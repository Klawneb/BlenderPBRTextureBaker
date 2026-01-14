# Changelog

## v1.1.3 - 14-01-2026
- Minimum supported Blender version updated from **4.4.0** to **5.0.0**
- Original render and bake settings are now captured before baking and restored after completion or cancellation preventing permanent changes to the user’s render engine and bake configuration
- Output path property now explicitly supports blend-relative paths
- Baking progress overlay text changed from centered alignment to left-aligned layout. Improved on-screen readability with fixed left margin for bake progress text
- Added logic to redirect texture output to "/tmp/textures/" with a warning if the output path is relative (//) and the blend file is unsaved.