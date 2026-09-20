# Lab 4 Reflection: Turtle Scene

## Encapsulation
Encapsulation basically meant hiding all the messy turtle steps inside separate functions. Instead of cluttering my main file with endless lines of `penup()`, `goto()`, `pendown()`, and angle turns, I bundled them into clean tools like `draw_square()`, `draw_pumpkin()`, and `draw_star()`. 

This made debugging way easier. For example, when the pumpkin stem drew in the wrong place or the mouth pointed backward, I knew exactly which function to open and tweak without worrying that I'd accidentally mess up the sky or the eyes.

## Generalization
Generalization was about making those functions flexible by using parameters instead of hardcoded numbers. 

An example was `draw_polygon(t, sides, length)`. Instead of writing one function for triangles and another for other polygons, one function handled both just by changing the `sides` argument. Giving functions parameters like `(x, y)` and `radius` also made building the composite scene simple—I could draw three jack-o'-lanterns at different positions and sizes across the screen without copying and pasting lines of code.

## Breaking Down the Scene
Putting it all together made a big drawing feel manageable. starting with basic geometry, combining shapes into  jack-o'-lanterns, and then placing them under a randomized night sky with  a handful of function calls.