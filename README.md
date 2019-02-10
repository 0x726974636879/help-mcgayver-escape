# Aidez McGayver à s'échapper.

It's a school project named "Help McGayver to escape".

Requirements :
- Python 3.6
- Pygame 1.9.4

EN (Soon):
...

FR :
> Vous venez de faire vos premiers pas avec Python et avez averti tous vos amis. Bravo ! Les réactions s'enchaînent sur votre mur Facebook et vous vous sentez l'âme d'une rock star avant la sortie de son dernier disque. Et là, c'est le drame : un troll a la bonne idée de commenter "Python ça sert à rien. Essaie plutôt Swift, tu pourras faire des jeux pour iOS". Ni une ni deux, vous décidez de créer un jeu pour montrer à votre "ami" de quel bois Python se chauffe.

Étant un grand fan de Richard Dean Anderson, vous imaginez un labyrinthe 2D dans lequel MacGyver aurait été enfermé.
La sortie est surveillée par un garde du corps dont la coiffure ferait pâlir Tina Turner.
Pour le distraire, il vous faut réunir les éléments suivants (dispersés dans le labyrinthe) :
- une aiguille
- un petit tube en plastique
- de l'éther

Ils permettront à MacGyver de créer une seringue et d'endormir notre garde.

### Fonctionnalités :
1. Il n'y a qu'un seul niveau.
2. La structure (départ, emplacement des murs, arrivée), devra être enregistrée dans un fichier pour la modifier facilement au besoin.
3. MacGyver sera contrôlé par les touches directionnelles du clavier.
4. Les objets seront répartis aléatoirement dans le labyrinthe et changeront d'emplacement si l'utilisateur ferme le jeu et le relance.
5. La fenêtre du jeu sera un carré pouvant afficher 15 sprites sur la longueur.
6. MacGyver devra donc se déplacer de case en case, avec 15 cases sur la longueur de la fenêtre !
7. Il récupèrera un objet simplement en se déplaçant dessus.
8. Le programme s'arrête uniquement si MacGyver a bien récupéré tous les objets et trouvé la sortie du labyrinthe. S'il n'a pas tous les objets et qu'il se présente devant le garde, il meurt (la vie est cruelle pour les héros).
9. Le programme sera standalone, c'est-à-dire qu'il pourra être exécuté sur n'importe quel ordinateur.
