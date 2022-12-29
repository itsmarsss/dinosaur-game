<h1 align="center">
<img src="/assets/dead.png" alt="Icon" width="100" height="100">
<br>
DinosaurGame
<br>
</h1>

## NOTICE
> :warning: :warning: :warning: **WARNING:** This project is no longer maintained; there may be bugs. Feel free to fork this repository, pull requests *may* be accepted. :warning: :warning: :warning:

## What is DinosaurGame
DinosaurGame is a parody of Chrome's hidden Dinosaur game. DinosaurGame will provide a similar experience, but you can turn on autoplay whenever you desire.

## Download
### Cloning
You can clone the repository by doing the following:  
`git clone https://github.com/itsmarsss/DinosaurGame.git`  
You can run it in an IDE or build it into an executable, up to you.

#### Build Project
Make sure to move everything out of `assets` folder.

Make sure to 
```py
import sys
```

Make sure to update line `17` to `60` to the following:  
```py
bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
RUN1 = pygame.image.load(os.path.abspath(os.path.join(bundle_dir, 'run-1.png')))
RUN2 = pygame.image.load(os.path.abspath(os.path.join(bundle_dir, 'run-2.png')))
DUCK1 = pygame.image.load(os.path.abspath(os.path.join(bundle_dir, 'duck-1.png')))
DUCK2 = pygame.image.load(os.path.abspath(os.path.join(bundle_dir, 'duck-2.png')))
DEAD = pygame.image.load(os.path.abspath(os.path.join(bundle_dir, 'dead.png')))
BIRD1 = pygame.image.load(os.path.abspath(os.path.join(bundle_dir, 'bird-1.png')))
BIRD2 = pygame.image.load(os.path.abspath(os.path.join(bundle_dir, 'bird-2.png')))
SMALL1 = pygame.image.load(os.path.abspath(os.path.join(bundle_dir, 'small-1.png')))
SMALL2 = pygame.image.load(os.path.abspath(os.path.join(bundle_dir, 'small-2.png')))
SMALL3 = pygame.image.load(os.path.abspath(os.path.join(bundle_dir, 'small-3.png')))
LARGE1 = pygame.image.load(os.path.abspath(os.path.join(bundle_dir, 'large-1.png')))
LARGE2 = pygame.image.load(os.path.abspath(os.path.join(bundle_dir, 'large-2.png')))
LARGE3 = pygame.image.load(os.path.abspath(os.path.join(bundle_dir, 'large-3.png')))
CLOUD = pygame.image.load(os.path.abspath(os.path.join(bundle_dir, 'cloud.png')))
RESTART = pygame.image.load(os.path.abspath(os.path.join(bundle_dir, 'restart.png')))
GROUND = pygame.image.load(os.path.abspath(os.path.join(bundle_dir, 'ground.png')))

RUN1 = pygame.transform.scale(RUN1, (RUN1.get_width() / 2, RUN1.get_height() / 2))
RUN2 = pygame.transform.scale(RUN2, (RUN2.get_width() / 2, RUN2.get_height() / 2))
DUCK1 = pygame.transform.scale(DUCK1, (DUCK1.get_width() / 2, DUCK1.get_height() / 2))
DUCK2 = pygame.transform.scale(DUCK2, (DUCK2.get_width() / 2, DUCK2.get_height() / 2))
DEAD = pygame.transform.scale(DEAD, (DEAD.get_width() / 2, DEAD.get_height() / 2))

GROUND = pygame.transform.scale(GROUND, (GROUND.get_width() / 2, GROUND.get_height() / 2))
CLOUD = pygame.transform.scale(CLOUD, (CLOUD.get_width() / 2, CLOUD.get_height() / 2))
RESTART = pygame.transform.scale(RESTART, (RESTART.get_width() / 2, RESTART.get_height() / 2))

BIRD1 = pygame.transform.scale(BIRD1, (BIRD1.get_width() / 2, BIRD1.get_height() / 2))
BIRD2 = pygame.transform.scale(BIRD2, (BIRD2.get_width() / 2, BIRD2.get_height() / 2))

SMALL1 = pygame.transform.scale(SMALL1, (SMALL1.get_width() / 2, SMALL1.get_height() / 2))
SMALL2 = pygame.transform.scale(SMALL2, (SMALL2.get_width() / 2, SMALL2.get_height() / 2))
SMALL3 = pygame.transform.scale(SMALL3, (SMALL3.get_width() / 2, SMALL3.get_height() / 2))

LARGE1 = pygame.transform.scale(LARGE1, (LARGE1.get_width() / 2, LARGE1.get_height() / 2))
LARGE2 = pygame.transform.scale(LARGE2, (LARGE2.get_width() / 2, LARGE2.get_height() / 2))
LARGE3 = pygame.transform.scale(LARGE3, (LARGE3.get_width() / 2, LARGE3.get_height() / 2))

JUMP_SOUND = pygame.mixer.Sound(os.path.abspath(os.path.join(bundle_dir, 'jump.mp3')))
POINT_SOUND = pygame.mixer.Sound(os.path.abspath(os.path.join(bundle_dir, 'point.mp3')))
DIE_SOUND = pygame.mixer.Sound(os.path.abspath(os.path.join(bundle_dir, 'die.mp3')))

FONT = pygame.font.Font(os.path.abspath(os.path.join(bundle_dir, 'PressStart2P-Regular.ttf')), 12)
```

Make sure to use pyinstaller in the directory of all files  
```
pyinstaller --add-data="run-1.png;." --add-data="run-2.png;." --add-data="bird-1.png;." --add-data="bird-2.png;." --add-data="cloud.png;." --add-data="dead.png;." --add-data="duck-1.png;." --add-data="duck-2.png;." --add-data="ground.png;." --add-data="large-1.png;." --add-data="large-2.png;." --add-data="large-3.png;." --add-data="small-1.png;." --add-data="small-2.png;." --add-data="small-3.png;." --add-data="restart.png;." --add-data="die.mp3;." --add-data="point.mp3;." --add-data="jump.mp3;." --add-data="PressStart2P-Regular.ttf;." -i="icon.ico" --noconsole --onefile "Dinosaur Game.py"
```


### Lazy download
If you're a lazy bum like me, head over to [[releases]](https://github.com/itsmarsss/DinosaurGame/releases), and download the most recent version.

## How To Play
### Options
#### [space key]/[up key]
Dino Jumps
#### [down key]
Dino ducks or falls faster
#### hold [A key]
Toggle autoplay
#### scroll [wheel]
Increase/Decrease volume
<!--
## Video (Shameless self promo)
[![Image Link](https://raw.githubusercontent.com/itsmarsss/AutoFlappy/main/assets/thumbnail.jpg)](https://www.youtube.com/watch?v=-sUVFuqVBdU)
-->