
# Crear y subir la rama feature/SCRUM-7
git checkout develop
git checkout -b feature/SCRUM-7
git push -u origin feature/SCRUM-7
git add .
git commit -m "[SCRUM-7] Implementar finestra flotant"

git push origin feature/SCRUM-7

# Crear y subir la rama feature/SCRUM-8
git checkout develop
git checkout -b feature/SCRUM-8
git push -u origin feature/SCRUM-8
git add .
git commit -m "[SCRUM-8] Funcionalitat finestra"
git push origin feature/SCRUM-8

# Crear y subir la rama feature/SCRUM-9
git checkout develop
git checkout -b feature/SCRUM-9
git push -u origin feature/SCRUM-9
git add .
git commit -m "[SCRUM-9] Aspectes estètics finestra"
git push origin feature/SCRUM-9

# Crear y subir la rama feature/SCRUM-11
git checkout develop
git checkout -b feature/SCRUM-11
git push -u origin feature/SCRUM-11
git add .
git commit -m "[SCRUM-11] Generador de contrasenyes"
git push origin feature/SCRUM-11

# Crear y subir la rama feature/SCRUM-12
git checkout develop
git checkout -b feature/SCRUM-12
git push -u origin feature/SCRUM-12
git add .
git commit -m "[SCRUM-12] Comprovador de contrasenyes"
git push origin feature/SCRUM-12

# Crear y subir la rama feature/SCRUM-13
git checkout develop
git checkout -b feature/SCRUM-13
git push -u origin feature/SCRUM-13
git add .
git commit -m "[SCRUM-13] Funció global del programa"
git push origin feature/SCRUM-13

# Una vez que una tarea esté lista para integrarse en main, fusiona los cambios

# Cambiar a la rama main y fusionar los cambios de la tarea SCRUM-7
git checkout main
git merge feature/SCRUM-7
git push origin main

# Fusiona siempre los cambios en develop también para mantener ambas ramas sincronizadas
git checkout develop
git merge main
git push origin develop

# Repetir los pasos para las demás tareas SCRUM-8, SCRUM-9, SCRUM-11, SCRUM-12, SCRUM-13
git checkout main
git merge feature/SCRUM-8
git push origin main
git checkout develop
git merge main
git push origin develop

git checkout main
git merge feature/SCRUM-9
git push origin main
git checkout develop
git merge main
git push origin develop

git checkout main
git merge feature/SCRUM-11
git push origin main
git checkout develop
git merge main
git push origin develop

git checkout main
git merge feature/SCRUM-12
git push origin main
git checkout develop
git merge main
git push origin develop

git checkout main
git merge feature/SCRUM-13
git push origin main
git checkout develop
git merge main
git push origin develop

# Crear una rama release (si es necesario para versiones)
git checkout develop
git checkout -b release/v1.0.0
git push -u origin release/v1.0.0

# Eliminar las ramas de funcionalidades cuando ya no las necesites

git branch -d feature/SCRUM-7
git branch -d feature/SCRUM-8
git branch -d feature/SCRUM-9
git branch -d feature/SCRUM-11
git branch -d feature/SCRUM-12
git branch -d feature/SCRUM-13

# Eliminar la rama remota
git push origin --delete feature/SCRUM-7
git push origin --delete feature/SCRUM-8
git push origin --delete feature/SCRUM-9
git push origin --delete feature/SCRUM-11
git push origin --delete feature/SCRUM-12
git push origin --delete feature/SCRUM-13

