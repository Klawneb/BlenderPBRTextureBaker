# Changelog

## v1.1.6 - 27-05-2026
- Added a UV Map dropdown for choosing which selected-object UV layer is used for baking
- Selected UV maps are temporarily set as active/render UVs during baking and restored afterward
- Added a warning when a chosen UV map is missing on one or more selected objects
- Material node and UV state cleanup now runs even if a per-object bake raises an error

## v1.1.5 - 27-05-2026
- Changed Normal map baking from Blender's native `NORMAL` bake type to the add-on's Emission bake workflow to avoid Blender 5.1 crashes
- Added support for baking normal textures from standard `Image Texture -> Normal Map -> Principled BSDF` node chains
- Normal baking now falls back to a flat normal map when no compatible normal texture source is found

## v1.1.4 - 27-05-2026
- Minimum supported Blender version updated from **5.0.0** to **5.1.0**
- Added Blender Extension packaging metadata with `blender_manifest.toml` and an `__init__.py` wrapper
- Added fallback lookup for renamed Principled BSDF sockets, including Specular / Specular IOR Level
- Guarded Cycles bake setting capture and restoration for Blender 5.1 compatibility
- Corrected Alpha and Normal output images to use Non-Color color space

## v1.1.3 - 14-01-2026
- Minimum supported Blender version updated from **4.4.0** to **5.0.0**
- Original render and bake settings are now captured before baking and restored after completion or cancellation preventing permanent changes to the user’s render engine and bake configuration
- Output path property now explicitly supports blend-relative paths
- Baking progress overlay text changed from centered alignment to left-aligned layout. Improved on-screen readability with fixed left margin for bake progress text
- Added logic to redirect texture output to "/tmp/textures/" with a warning if the output path is relative (//) and the blend file is unsaved.
