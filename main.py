colors = ["slate",
          "gray",
          "zinc",
          "neutral",
          "stone",
          "red",
          "orange",
          "amber",
          "yellow",
          "lime",
          "green",
          "emerald",
          "teal",
          "cyan",
          "sky",
          "blue",
          "indigo",
          "violet",
          "purple",
          "fuchsia",
          "pink",
          "rose", ]

opacities = ["50", "100", "200", "300",
             "400", "500", "600", "700", "800", "900"]

types = ["bg", "text", "border"]

for color in colors:
    for opacity in opacities:
        for type in types:
            print('<div className="'+type+"-"+color+"-"+opacity+'" />')
