# PRINCIPIOS SOLID Y CLEAN CODE

## 1. Single Responsibility Principle (SRP)

-    Header: Este componente se encarga de renderizar el encabezado con un formulario de inicio de sesión. Está bien separado y tiene una única responsabilidad.

-    HeaderLobby: Este componente se encarga de renderizar el encabezado para la página del lobby con opciones de navegación y botones. También cumple con el principio de responsabilidad única.
## 2. Interface Segregation Principle (ISP)

-   En React, este principio se relaciona con pasar solo las props necesarias a los componentes. Ambos componentes están bien en este sentido, ya que no están pasando más props de las necesarias.

## Practicas CLEAN CODE usadas

###    Funciones pequeñas:
-    Tanto Header como HeaderLobby son componentes pequeños que cumplen con el principio de tener una única responsabilidad.

###    Nombres significativos:
 -    Los nombres de las funciones (Header, HeaderLobby) y las clases CSS (container, login-form, input-email, etc.) son descriptivos y claros.

###    Uso de constantes y funciones:
-    handleLoginClick es una función separada, lo cual mejora la legibilidad y facilita el mantenimiento del código.

## Código usado

```bash
import React from 'react';

export const Header = () => {
  return (
    <header>
      <div className="container">
        <h1>PASSUX</h1>
        <div className="login-form">
          <input type="email" placeholder="Correo" className="input-email" />
          <input type="password" placeholder="Contraseña" className="input-password" />
          <button className="login-btn" >Login</button>
        </div>
      </div>
    </header>
  );
};

export const HeaderLobby = () => {
  const handleLoginClick = () => {
    window.location.href = `/register.html`;
  };
  return (
    <header>
      <div className="container">
        <img src="src/static/img/perfil.png" alt="Logoo" className="logo" />
        <img src="src/static/img/welcome.png" alt="welcome" className="welcome" />
        <nav>
          <a>Contact</a>
          <button className="sign-in">Sign in</button>
          <button className="register" onClick={handleLoginClick}>Register</button>
        </nav>
      </div>
    </header>
  );
};
```

## 1. Single Responsibility Principle (SRP)

-    Lobby: Este componente tiene la responsabilidad única de ensamblar y renderizar otros componentes (HeaderLobby, MainLobby, AnuncioLobby, y Footer). Cumple c       con el principio de responsabilidad única ya que no tiene lógica adicional y solo se encarga de la composición de la interfaz.

## 2. Liskov Substitution Principle (LSP)

-    En el contexto de componentes de React, cualquier componente que cumpla con la misma interfaz (recibe las mismas props) podría sustituir a otro sin alterar el     comportamiento del Lobby.

## 3. Interface Segregation Principle (ISP)

-    Lobby: No fuerza a los componentes a depender de props que no usan. Cada componente (HeaderLobby, MainLobby, AnuncioLobby, y Footer) está diseñado para recibir y usar solo las props necesarias.

## Practicas CLEAN CODE usadas

### Funciones pequeñas:

-    Lobby es una función pequeña que solo se encarga de ensamblar y renderizar otros componentes.

### Nombres significativos:

-    Los nombres de las funciones (Lobby, HeaderLobby, MainLobby, AnuncioLobby, Footer) son descriptivos y reflejan claramente su propósito

## Código usado
```bash
import React from 'react';
import {HeaderLobby} from './components/Header.jsx';
import {MainLobby,AnuncioLobby} from './components/Main.jsx';
import Footer from './components/Footer.jsx';

const Lobby = () => {
  return (
    <div>
      <HeaderLobby />
      <MainLobby />
      <AnuncioLobby/>
      <Footer />
    </div>
  );
};

export default Lobby;
```

## 1. Dependency Inversion Principle (DIP)

-    Este código depende directamente de ReactDOM y Register, lo cual está bien en este contexto.
   
## 2. Single Responsibility Principle (SRP)

-    Este código tiene una única responsabilidad: renderizar el componente Register en un elemento del DOM con el ID register. Cumple con el principio de responsabilidad única porque cada parte del código tiene un propósito claro:

-        Importar dependencias (React, ReactDOM).
-        Importar el componente Register.
-        Importar los estilos CSS.
-        Renderizar el componente Register.

## Practicas CLEAN CODE usadas 

### Single Responsibility Principle (SRP):

-    Este código tiene una única responsabilidad: renderizar el componente Register en un elemento del DOM con el ID register.

### Nombres significativos:

-    Los nombres de las funciones y las importaciones (Register, ReactDOM.render) son claros y descriptivos.

### Código limpio y conciso:

-    El código es breve y al grano, importando solo las dependencias necesarias y realizando una única acción claramente definida.

## Código usado
```bash  
import React from 'react';
import ReactDOM from 'react-dom';
import Register from './Register';
import './static/Register.css';


ReactDOM.render(<Register />, document.getElementById('register'));
```


















