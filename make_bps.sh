#!/usr/bin/env bash
# Builds the release ROM and creates a BPS patch against a clean Pokémon Emerald (USA) ROM,
# then checks that applying the patch gives back the exact release ROM.
#
# Usage: ./make_bps.sh [clean_emerald_us.gba]   (path relative to the repo root)
# Env:   FLIPS = path to the Flips executable (default: ../tools/flips)

set -euo pipefail
cd "$(dirname "$0")"

BASE_ROM="${1:-../rom/emerald_us.gba}"
BASE_SHA1="f3ae088181bf583e55daf962a92bb46f4f1d07b7"
FLIPS="${FLIPS:-../tools/flips}"
RELEASE_ROM="pokeemerald-release.gba"
PATCH="build/pokemon_nabla.bps"

sha1() {
    if command -v sha1sum > /dev/null; then sha1sum "$1"; else shasum -a 1 "$1"; fi | cut -d ' ' -f 1
}

if [[ ! -f "$BASE_ROM" ]]; then
    echo "Base ROM not found: $BASE_ROM" >&2
    exit 1
fi
if [[ "$(sha1 "$BASE_ROM")" != "$BASE_SHA1" ]]; then
    echo "Base ROM is not a clean Pokémon Emerald (USA): $BASE_ROM" >&2
    exit 1
fi
if ! command -v "$FLIPS" > /dev/null; then
    echo "Flips not found. Install it or set FLIPS=/path/to/flips." >&2
    exit 1
fi

make release -j"$(getconf _NPROCESSORS_ONLN)"

mkdir -p build
"$FLIPS" --create --bps-delta "$BASE_ROM" "$RELEASE_ROM" "$PATCH"

CHECK_ROM="$(mktemp)"
trap 'rm -f "$CHECK_ROM"' EXIT
"$FLIPS" --apply "$PATCH" "$BASE_ROM" "$CHECK_ROM" > /dev/null
if [[ "$(sha1 "$CHECK_ROM")" != "$(sha1 "$RELEASE_ROM")" ]]; then
    echo "Patch check failed: patched ROM differs from $RELEASE_ROM" >&2
    exit 1
fi

echo "Patch: $PATCH ($(wc -c < "$PATCH" | tr -d ' ') bytes)"
echo "Patched ROM SHA1: $(sha1 "$RELEASE_ROM")"
