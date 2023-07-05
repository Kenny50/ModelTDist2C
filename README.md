# Tainan modelT distance to color

## require project
[TainanModelT](https://github.com/Kenny50/TainanModelT)
## service architecture
```
                                     _________________
                                    |                 |
   Redis Channel `point-cloud` ---->|     Python      | point_cloud.py
 [ { x: float, y: float, z: float} ]|                 |
                                    |_________________|
                                               |
                                               |
                                               V
                                    _________________
                                   |                 |
                 Convert Coordinates to Distance     | coordinate_to_distance.py
                                   |_________________|
                                               |
                                               |
                                               V
                                    _________________
                                   |                 |
                          Get Color from Colormap    | color_conversion.py
                                   |_________________|
                                               |
                                               |
                                               V
                                    _________________
                                   |                 |
                       Convert Color to RGB Values   | color_conversion.py
                                   |_________________|
                                               |
                                               |
                                               V
                  Make HTTP POST Request to `http://host.docker.internal:3000/d2color`
```
