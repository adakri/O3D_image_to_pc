## o3d_png_converter: generatig surface point clouds from images

> :warning: **This work is very rudimentery at this stage (and maybe will be that forever):** a lot of ideas regarding compression, curvature alignment are coming up, and a whole bunch of technical integration issues are popping off.


Sometimes, when doing modelling or simulation, one needs to put colored surfaces on 3D flat surfaces. Images are usually used to generate textured surfaces, but there is not a tool to do this automatocally. This repository tries to solve this problem using the Open3D librairy for point cloud processing. The idea of this tool was to simply make it easier to texture point cloud surfaces without needing to go through Meshlab's tools (which is very possible and extremely convenient and simple), but what is going to be more convenient is the ability to integrate such a tool in [Open3D](http://www.open3d.org/), the leading point cloud processing librairy.



An example of use, this is an image:
<p align="center">
	<img src="https://github.com/adakri/O3D_image_to_pc/blob/master/img/sample.jpg?raw=true" width="640" height="480">
</p>

This its associated point cloud (> :interrobang: the resolution is fixed, no compression is done and it takes some time, but it works)
<p align="center">
	<img src="https://github.com/adakri/O3D_image_to_pc/blob/master/img/result.png?raw=true" width="640" height="480">
</p>
