# Tailwind Classes Generator

Due to an awful bug with Tailwind and JSX conditional classes, I needed to create this tool in order for my colors/styles to actually work when I use that in my projects.

This is currently only creating every single color for `bg` and `text` elements, but this script can easily be modified to do anything you want by adding to the 3 arrays.

## How to run it

> You need to have python installed in order to run this script.

```shell
python3 main.py
```

This will print all of the classes to console which you can then copy to a file in your project, like you can see [here](https://github.com/DavidIlie/davidilie.com/blob/master/frontend/src/components/tailwindbad.tsx)
