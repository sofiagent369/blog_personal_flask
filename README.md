2. **Acceder a la Aplicación**

   - Página Principal: [http://localhost:5000](http://localhost:5000)
   - Panel Admin (requiere autenticación): [http://localhost:5000/admin](http://localhost:5000/admin)

3. **Autenticación**

   - Registrar un nuevo usuario: `/api/auth/register`
   - Iniciar sesión: `/api/auth/login`
   - Cerrar sesión: `/api/auth/logout`

4. **Interacciones con Posts**

   - Listar posts: `GET /api/posts`
   - Crear post: `POST /api/posts` (requiere autenticación)
   - Actualizar post: `PUT /api/posts/<post_id>` (requiere autenticación)
   - Eliminar post: `DELETE /api/posts/<post_id>` (requiere autenticación)

## Contribución

1. **Fork** el repositorio.
2. **Crea** una nueva rama (`git checkout -b feature/AmazingFeature`).
3. **Hacer commit** de tus cambios (`git commit -m 'Añade algún gran cambio'`).
4. **Pushea** a la rama (`git push origin feature/AmazingFeature`).
5. Abre un `Pull Request`.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT.