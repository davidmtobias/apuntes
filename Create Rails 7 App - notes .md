# 1. Configurar una aplicación Rails 7 completa desde cero

## 1.1 Características
Vite + Vue + Vanilla Javascript + Tailwincss + Sprockets (compilación assets tradicional) + No Importmaps

## 1.2 Instalación

### 1. Creamos una aplicación básica SIN importmaps

``rails new myAppName --asset-pipeline=sprockets --skip-test --skip-system-test --skip-bootsnap --skip-hotwire --skip-action-mailer --skip-action-mailbox --skip-action-text --skip-active-job --skip-active-storage --skip-action-cable --skip-javascript``

* He añadido: **--skip-javascript** para que no instale importmaps.

* Con "--skip-bundle" y CON "--skip-javascript" (no importmaps), NO ejecuta:
  
  ``bundle install``
  ``bundle lock --add-platform=x86_64-linux``
  ``bundle binstubs bundler``

* Con "--skip-bundle" y sin "--skip-javascript" (con importmaps) y , NO ejecuta:
  ``bundle install``
  ``bundle lock --add-platform=x86_64-linux``
  ``bundle binstubs bundler``
  ``rails  importmap:install``
  ``bundle install``

### 2. Configuración básica de la aplicación

Evitamos generar archivos no usados en los scaffold generator. En **config/application.rb**

    config.generators do |g|
      g.test_framework nil
      g.system_tests nil
      #g.template_engine nil #Quita las vistas
      g.assets false
      g.helper false
      g.jbuilder false
      g.stylesheets false
      g.javascripts false
    end

O tan bien:

    config.generators.helper = false
    config.generators.assets = false
    [...]

### 3. Creamos la estructura Javascript para VUE, Sprockets y fake Importmaps

#### 3.1 Sprockets

Nota: Los javascript los guardamos en **app/assets**, si no, me da el siguiente error:
**The asset "application.js" is not present in the asset pipeline.**

Será publicado con **<%= javascript_include_tag "application", "data-turbo-track": "reload", defer: true %>**

En **assets/config/manifest.js**, añadimos lo siguiente para que Sprockets funcione:

    //= link_tree ../images
    //= link_directory ../stylesheets .css
    //= link_tree ../javascript .js
    //= link_tree ../../../vendor/javascript .js

Creamos **app/assets/javascript/sprockets/index.js**

    //= require "./test"

Creamos **app/assets/javascript/sprockets/test.js**

    console.log("Test sprocket")

Creamos **app/assets/javascript/application.js**

    // SPROCKETS
    //
    // CUIDADO: no puedo usar "imports" por este método: 
    // Error: Uncaught SyntaxError: Cannot use import statement     outside a module 
    //
    // Load by <%= javascript_include_tag "application",    "data-turbo-track": "reload", defer: true %>
    //
    // This is a manifest file that'll be compiled into     application.js, which will include all the files
    // listed below.
    //
    // Any JavaScript/Coffee file within this directory, lib/   assets/javascripts, or any plugin's
    // vendor/assets/javascripts directory can be referenced    here using a relative path.
    //
    // It's not advisable to add code directly here, but if you     do, it'll appear at the bottom of the
    // compiled file. JavaScript code in this file should be    added after the last require_* statement.
    //
    // Read Sprockets README (https://github.com/rails/   sprockets#sprockets-directives) for details
    // about supported directives.
    //
    // require jquery
    // Unostrusive javascript de Rails. Necesario para que los    métodos delete envíen un delete y no un get.
    // require rails-ujs 
    // require_tree .
    //= require sprockets


#### 3.2 Vue

Será enlazado a través de Vite mediante el archivo **javascript/entrypints/application.js** que creamos en los puntos siguientes.


Añado **app/javascript/vue/components/App.vue**:

    <template lang="">
      <div class="bg-indigo-700">
        <h1>Vue Great</h1>
      </div>
      <counter></counter>
    </template>

    <script setup>
      import { ref } from "vue";
      import Counter from "./Counter.vue"

      // let counter = ref(0);
      // const incrCounter = function() {
      // 	counter.value += 1;
      // }	
      </script>

    <style lang="">

    </style>

Añado **app/javascript/vue/components/Counter.vue**:

    <template lang="">
      <div>
          <button @click="increment" id="counter-button">Increment</   button>
          <p>Count is s: {{ count }}</p>
          <p></p>
          <div class="box bg-lime-200">Qué tal
              <h1>Automatico</h1>
          </div>
          <div class="bg-yellow-200">
              Hola
          </div>
      </div>
    </template>

    <script setup>
      import { ref } from "vue";  
      let count = ref(0);
      const increment = function() {
        count.value += 6;
      }
    </script>

    <style lang="scss">
      #counter-button {
        background-color: green;
        border-radius: 5px;
        padding: 30px;
        color: #fff;
        font-size: 1.2em;
        border: none;
      }

      .box2 {
        background-color: green;
        h1 {
          color: red;
        }
      }
    </style>

#### 3.3 Importmaps (fake)

Hemos deshabilitado importmaps en nuestra aplicación pero podemos cargar javascript mediante imports de esta forma.

Será enlazado a través de Vite mediante el archivo **javascript/entrypints/application.js** que creamos en los puntos siguientes.


Creo **app/javascript/application-imports.js**:

    // Configure your import map in config/importmap.rb. Read more: https://github.com/rails/importmap-rails
    import "./imports/exec"


Creo **app/javascript/imports/mi_modulo.js**:

    let number = 42;
    const hello = (param) => "Hello!"+param;
    const goodbye = () => "¡Adiós!";
    class CodeBlock { };

    console.log("Ejecuto mi modulo import/export way")

    number+=1;

    export {
      number,
      hello,
      goodbye as bye,
      hello as greet
    };

Creo **app/javascript/imports/exec.js**:

    import { hello, number } from "./mi_modulo"

    // HMR code
    console.log(hello("David Merino"));
    console.log(number);

#### 3.4 Creo app/vendor/javascript

En esta carpeta puedo meter por ejemplo: **jquery.min.js**



### 4. Instalamos y configuramos VITE + VUE

#### 4.1 Instalamos VITE RUBY

``gem "vite_rails"``
``bundle install``
``bundle exec vite install``

#### 4.2 Full Reload para vite

``npm i vite-plugin-full-reload @vitejs/plugin-vue vue``

#### 4.3 Instalamos y configuramos VUE con VITE

El plugin @vitejs/plugin-vue me permite usar VUE en el contexto VITE.
   
``npm i @vitejs/plugin-vue vue``

#### 4.4 Archivo de configuración de vite "vite.config.ts"

    import { defineConfig } from "vite";
    import RubyPlugin from "vite-plugin-ruby";
    import FullReload from "vite-plugin-full-reload";

    // ¿Como detecto los cambios refrescar?
    // En tailwindo.config.js se añaden los archivos a    inspeccionar para leer las etiquetas html y
    // y posteriormente "rebuild" "app/assets/builds/tailwind.    css"
    //
    // Aquí en vite.config.ts pongo los archivos a monitorizar    para lanzar un FullReload
    //
    // 1. VUE: Los archivos .vue se actualizan por HMR. Además,     si el estilo no está
    // 1.1 Ocurre que: cambio en una clase de algún elemento    html del .vue =>
    // => tailwind lo detecta => modificación de builds/    tailwind.css => PAGE RELOAD
    //
    // 2. VANILLA JAVASCRIPT: Los cambios en javascript vanilla     los detectamos por vite.
    // Solo especifico los .js, no los .vue. FullReload con     "app/javascript/**/*.js"
    //
    // 3. VISTAS.
    // Problema: Al no tener HMR, no podemos confiar únicamente     en la modificación builds/tailwind.css
    // ya que si existe un cambio de texto, no lo detecta. Si     se cambia una clase ya existente,
    // no se modificará builds/tailwind.css y por tanto no    habrá refresco.
    //
    // Solución: poner: "app/views/**/*" aquí
    //
    // 4. ESTILOS
    // FullReload con "app/assets/stylesheets/**/*.*"

    import vue from "@vitejs/plugin-vue";

    export default defineConfig({
      clearScreen: false,
      plugins: [
        RubyPlugin(),
        FullReload(
          [
            "config/routes.rb",
            "app/javascript/**/*.js",
            "app/assets/builds/tailwind.css",
            "app/views/**/*",
            "app/assets/stylesheets/**/*.*",
          ],
          { delay: 200 }
        ),
        vue(),
      ],
      root: "./app/assets",
      build: {
        manifest: true,
        rollupOptions: {
          input: "/app/javascript/entrypoints/application.js",
        },
      },
    });


#### 4.5 Enlace con imports

Enlazamos los javascript que se cargarán con *imports* en **javascript/entrypoints/application.js.**

Escribo al final del archivo:

    // Imports
    // No uso gem "importmap-rails"; pero puedo emularlo de     esta manera.
    // Antes de la carga de VUE, para que refresque con Vite    Ruby
    import "../application-imports.js"

#### 4.6 Habilitamos VUE

Nota: En "entrypoints" es donde VITE lee para crear los empaquetados que serán publicados a través de **<%= vite_javascript_tag 'application' %>**

Añado al final de **javascript/entrypints/application.js**

    // Create Vue App
    import { createApp } from "vue";

    // Import App Component
    import App from "../vue/components/App.vue";

    // Create Vue App
    const app = createApp(App).mount("#app");

### 5. Sass a través de Sprockets

Añadimos compilación de estilos mediante sass con Sprockets.

Será publicado mediante: **<%= stylesheet_link_tag "application" %>**

Instalo la gema de Sass, en **Gemflile**

    # Use Sass to process CSS (MINIMIFIED)
    gem "sassc-rails"

``bundle install``

Para que en los single file components se pueda uilizar scss:

``npm install -D sass`` o ``npm add -D sass``

Then you can use in your .vue file:

    <style lang="scss"></style>


Creo **assets/general/styles.scss**

    .prueba {
      background-color: green;
    }

En el clásico **app/assetes/stylesheets/application.css** enlazo los estilos mediante *require*:

    /*
     * This is a manifest file that'll be compiled into     application.css, which will include all the files
     * listed below.
     *
     * Any CSS (and SCSS, if configured) file within this     directory, lib/assets/stylesheets, or any plugin's
     * vendor/assets/stylesheets directory can be referenced    here using a relative path.
     *
     * You're free to add application-wide styles to this file    and they'll appear at the bottom of the
     * compiled file so the styles you add here take precedence     over styles defined in any other CSS
     * files in this directory. Styles in this file should be     added after the last require_* statement.
     * It is generally better to create a new file per style    scope.
     *
     *= require_tree ./general
     * require_tree .
     *= require_self
     */

     .prueba2 {
        background-color: red;
      }

Nota:
- Importante por el orden.
- require_self mete todos los estilos definidos en el propio applicatoin.css en función del orden
- require_tree mete todos los que estén en el directorio


### 6. Adding Tailwind

Fuente: https://github.com/rails/tailwindcss-rails

#### 6.1 Instalamos tailwind

``./bin/bundle add tailwindcss-rails``
``./bin/rails tailwindcss:install``

Será accesible via: **<%= stylesheet_link_tag "tailwind", "inter-font", "data-turbo-track": "reload" %>**

Nota: En **vite.config.ts** ya configuramos VITE para que detectara cambios en el build de Tailwind.

#### 6.2 Configuramos para que rastree los archivos ".vue"

En **app/config/tailwind.config.js**:

const defaultTheme = require('tailwindcss/defaultTheme')

    module.exports = {
      content: [
        './public/*.html',
        './app/helpers/**/*.rb',
        './app/javascript/**/*.vue',
        './app/views/**/*.{erb,haml,html,slim}'
      ],
      theme: {
        extend: {
          fontFamily: {
            sans: ['Inter var', ...defaultTheme.fontFamily.   sans],
          },
        },

      },
      plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/aspect-ratio'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/container-queries')
      ]
    }


### 7. Foreman para arrancar el entorno de desarrollo:

Me aseguro de que exista: **bin/dev**

    #!/usr/bin/env sh

    if ! gem list foreman -i --silent; then
      echo "Installing foreman..."
      gem install foreman
    fi

    exec foreman start -f Procfile.dev "$@"

Configuro **Procfile.dev** para arrancar los procesos que necesito.

    vite: bin/vite dev
    web: bin/rails s
    css: bin/rails tailwindcss:watch


### 8. Creación de la base de datos y primera migración

    rails db:create
    rails generate scaffold Coches marca:string modelo:string
    rails db:migrate

# 2. APP simple con Rails 7

## 2.1 Características
Vanilla Javascript + Sprockets (compilación assets tradicional)

## 2.2 Instalación

### 1. Creamos una aplicación básica SIN importmaps

``rails new myapp --asset-pipeline=sprockets --skip-test   --skip-system-test --skip-bootsnap --skip-hotwire  --skip-action-mailer --skip-action-mailbox   --skip-action-text --skip-active-job --skip-active-storage  --skip-action-cable --skip-javascript --skip-bundle``

* Añado: **--skip-javascript** para que no instale importmaps.
Manualmente tendré que meter las carpetas y los puntos de acceso.

* Si no pongo **--skip-javascript** añade ``gem importmaps``en **Gemfile**

* Si pongo **--javascript=esbuild** añade ``gem jsbundling-rails`` y ``gem cssbundling-rails``. Además, modifica la *task: rails assets:precompile* y busca en **Gemfile** ``yarn build`` y ``yarn build:css``. Y no quiero nada de esto



### 2. Añado gemas necesarias para la compilación de assets

En **Gemfile**

Uso Sass to process CSS + process JS con terser para minimificar el javascript.

``gem "sassc-rails"``
``gem 'terser``

``bundle install``

En **config/environments/production.rb**

    # Compress CSS using a preprocessor.
    config.assets.css_compressor = :sass

    # Compress JS
    config.assets.js_compressor = :terser
  
-  Con *terser* al hacer hago ``RAILS_ENV=production assets:precompile`` minimifica el javascript.



### 3. Carpetas para javascript y etilos

Creo **assets/javacript/application.js** con formato Sprockets:

    //= require vanilla

Creo **assets/vanilla/index.js**

    //= require "./prueba"

Creo **assets/vanilla/prueba.js**    

    console.log("VanillaJs is running")

Creo **assets/stylesheets/application.css**

    /*
     * This is a manifest file that'll be compiled into application.css,     which will include all the files
     * listed below.
     *
     * Any CSS (and SCSS, if configured) file within this directory, lib    /assets/stylesheets, or any plugin's
     * vendor/assets/stylesheets directory can be referenced here using a    relative path.
     *
     * You're free to add application-wide styles to this file and they'll     appear at the bottom of the
     * compiled file so the styles you add here take precedence over styles    defined in any other CSS
     * files in this directory. Styles in this file should be added after the    last require_* statement.
     * It is generally better to create a new file per style scope.
     *
     *= require_tree .
     *= require_tree ./general
     *= require_self
     */

Creo **assets/stylesheets/general/styles.scss**
  
    .prueba {
      background-color: green;
    }


En el manifest de Sprockets **assets/config/manifest.js**

    //= link_tree ../images
    //= link_directory ../stylesheets .css
    //= link_directory ../javascript .js

Publico los assetsw en el layout **application.html.erb**

    <%= javascript_include_tag "application" %>
    <%= stylesheet_link_tag "application" %>


### 4. Pruebas en PRODUCTION en LOCAL

En **config/environments/production.rb**, y solo para pruebas de produccón en local, servimos assets desde rails.

    # Disable serving static files from the `/public` folder by default since Apache or NGINX already handles this.
    # config.public_file_server.enabled = ENV["RAILS_SERVE_STATIC_FILES"].present?

    # Sirve assets desde rails
    config.public_file_server.enabled = true

    # Default Sirve assets desde servidor externo
    # config.public_file_server.enabled = false 

O también, si modificar **production.rb** 

``RAILS_ENV=production RAILS_SERVE_STATIC_FILES=true rails s``

Migro la base de datos y compilo:

``RAILS_ENV=production rails db:migrate``
``RAILS_ENV=production assets:precompile``
``RAILS_ENV=production rails s``

* **Cuidado a volver a development**. Al haber generado unas assets en **public**, el navegador cachea y por tanto hay que borrar las assets de public para que refresque los nuevos cambios en modo *devolpment*.

### 5. Browsersync

#### 5.1 Instalación: 

``npm install -g browser-sync``

#### 5.2 Configuración: 

En **config/bs-config.js**

    /**
     * Browsersync Config File
     * https://browsersync.io/docs/options
     */

    module.exports = {
      //server: '.',
      //proxy: 'localhost:3000',
      port: 3001,
      proxy: {
        target: "localhost:3000",
        proxyReq: [
          function(proxyReq) {
            /**
             * proxyReq.setHeader('X-Forwarded-Host', 'localhost:3001'); //   Evita errores de Token en Rails
             * Pongo la ip para acceder siempre a traves de ahí para permitir     varios dispositivos y no tener que diferenciar entre
             * localhost e ip
            */
              proxyReq.setHeader('X-Forwarded-Host', '192.168.43.   254:3001'); //Evita errores de Token en Rails
              //Para evitar errores de token accedo directamente por la ip    externa que me ofrece BrowserSync
          }
        ],
      },
      files: [
        'app/assets/stylesheets/*.scss',
        'app/assets/stylesheets/*/*.scss',
        'app/assets/stylesheets/*/*/*.scss',
        'app/assets/stylesheets/*/*/*/*.scss',
        'app/assets/stylesheets/*/*/*/*/*.scss',
        'app/views/*.html.erb',
        'app/views/*/*.html.erb',
        'app/views/*/*/*.html.erb',
        'app/views/*/*/*/*.html.erb',
        'app/views/*/*/*/*/*.html.erb',
        // 'app/javascript/*.vue', USO UN HOT RELOAD PARA VUE:    webpack-dev-server
        // 'app/javascript/*/*.vue',
        // 'app/javascript/*/*/*.vue',
        // 'app/javascript/*/*/*/*.vue',
        // 'app/javascript/*/*/*/*/*.vue'
        'app/assets/javascript/*.js',
        'app/assets/javascript/*/*.js',
        'app/assets/javascript/*/*/*.js',
        'app/assets/javascript/*/*/*/*.js',
        'app/assets/javascript/*/*/*/*/*.js'

      ],
      ui: false,
      //notify: false


      //Configuration for turbolinks. Evitar página en blanco
      snippetOptions: {
        rule: {
          match: /<\/head>/i,
          fn: function (snippet, match) {
            return snippet + match;
          }
        }
      }
    };


    //Puedo hacer live reload con browser-sync o con webpack-dev-server
    //Para recargar las assets cargadas con Sprockets => browser-sync

    //Para recarga todos los packs (vue) => webpack-dev-server
    //Además si uso hmr:true => solo carga la parte de vue modificada
    //Para que se entere de los cambios en los scss => hmr:false

    //Aún así, hacer un livereload tanto si cambio vue como si cambio las     scss solo es posible descomentando lo anterior en files; pero es    demasiado lento.
    //Por tanto: 
    //Uso localhost:3000 con webpack-dev-server para livereload (+hmr) en VUE     (Rails sabe como gestionarlo)
    //Uso la ip:3001 con browsersync para livereload de html y scss
    //Tendré el inconveniente de tenr que cambiar de pestaña en el navegador.     O cambio vue o cambios html/scss

    //Para live reload de todo lo que no sean packs .. browsersync
    //Para live reload de webpacker -- => webpack-dev-server
    //Este es un servidor de desarrollo que publicará los recursos de webpack     para que sean accesibles desde el navegador. 

    //browser-sync start --proxy localhost:3000 --files "app/assets/    stylesheets/*.scss, app/views/*/*/*.html.erb"
    //$ browser-sync start --config 'config/bs-config.js'

    //Para un hot reload de vue usar: webpack-dev-server --mode development
    //ejecuto bin/webpack-dev-server
    // tambien puedo npm run serve => porque está configurado en package.json
    // Hace live reload y hot module replacement
    // Webpack Dev Server no escribe los archivos tras compilar: los mantiene     en memoria. Por eso no los veremos en el acostumbrado directorio /dist.
    //Directamente recarga localhost:3000 

    // En webpacker.yml
    // Live reload hmr: false
    // Live reload and hot module reloading hmr:true Sin embargo, verás que     al hacerlo perdemos el estado de la aplicación. Para conservarlo mientras     modificamos los archivos que la componen tenemos la opción de Hot Module    Reloading.
    //
    // Cómo se entera Rails que webpack-dev-server funciona?
    //https://github.com/rails/webpacker
    //Once you start this webpack development server, Webpacker will    automatically start proxying all webpack asset 
    //requests to this server. When you stop this server, 
    //Rails will detect that it's not running and Rails will revert back to     on-demand compilation 
    //if you have the compile option set to true in your config/webpacker.yml


#### 5.3 Browsesync con foreman

Browsesync con foreman

Creo el siguiente archivo **bin/dev"**

    #!/usr/bin/env bash

    if ! foreman version &> /dev/null
    then
    echo "Installing foreman..."
    gem install foreman
    fi
    
    foreman start -f Procfile.dev "$@"

Creo en la raíz del proyecto **Procfile.dev**

    web: bin/rails server -p 3000
    browsersync: browser-sync start --config 'config/bs-config.js'

Ejecuto 

``bin/dev``

### 6. Creo la base de datos

    rails db:create
    rails generate scaffold Usuarios nombre:string apellidos:string
    rails db:migrate

### 7. Añado un Framework CSS

En construcción ...


# 3. Conceptos en Rails 7

Visión general de nuevas funcionalidades:
https://rubyonrails.org/2021/12/15/Rails-7-fulfilling-a-vision

## 3.1 Importmaps

Por defecto Rails 7 viene con *importmaps*. Las otras opciones son *webpacker* y *esbuild-rails*. Se pueden configurar con la opción ``--javascript`` o ``-j``.

## 3.2 Esbuild y Terser

**Esbuild**, empaqueta y **Terser** comprime el javascript final.

``esbuild app/javascript/*.\_ --bundle --sourcemap --outdir=app/assets/builds --public-path=assets``

    app/assets/builds/application.js 253.0kb
    app/assets/builds/add_jquery.js 252.5kb
    app/assets/builds/application.js.map 463.2kb
    app/assets/builds/add_jquery.js.map 461.3kb

y si en **config/production.rb** tenemos

``config.assets.js_compressor = :terser``

lo comprime.

## 3.3 Hotwire

**Tutorial imprescindible**: https://www.hotrails.dev/

Viene por defecto. Podemos no activarlo con ``--skip-hotwire`` al instalar la aplicación.

Está divido en las siguientes partes:

- **TURBO**, the heart of howire, the speed of a single-page web application without having to write any JavaScript:
  - **TURBO DRIVE** (turbolinks is the ancestor of TurboDrive)
  - **TURBO FRAMES**
  - **TURBO STREAMS** 
- **STIMULUS**, a modest JavaScript framework for the HTML you already have.
- **STRADA** (for mobile)

**Turbo Drive** is the first part of Turbo, which gets installed by default in Rails 7 applications, as we can see in our Gemfile and our JavaScript manifest file application.js.

By default, **Turbo Drive** speeds up our Ruby on Rails applications by converting all link clicks and form submissions into AJAX requests. That means that our CRUD application from the first chapter is already a single-page application, and we had no custom code to write.

With **Turbo Drive**, our Ruby on Rails applications will be fast by default because the HTML page we first visit won't be completely refreshed. When Turbo Drive intercepts a link click or a form submission, the response to the AJAX request will only serve to replace the ``<body>`` of the HTML page. In most cases, the ``<head>`` of the current HTML page won't change, resulting in a considerable performance
improvement: the requests to download the fonts, CSS, and JavaScript files will only be made once when we first access the website.

That's why new Ruby on Rails 7 applications are single-page applications by default. The page we first visit won't be completely replaced; only the ``<body>`` tag will.

Note: If you've been working with Rails for some time, you might be familiar with Turbolinks. Turbolinks is the ancestor of Turbo Drive: it only intercepted clicks on links but not form submissions. Now that Turbo also handles form submissions, the authors renamed the library from Turbolinks to Turbo Drive.

In most cases, Turbo Drive only replaces the ``<body>`` of the HTML page and leaves the ``<head>`` unchanged. I say in most cases because there are situations where we want Turbo Drive to notice changes on the ``<head>`` of our web pages.

To solve this problem, on every new request, Turbo Drive compares the DOM elements with data-turbo-track="reload" in the ``<head>`` of the current HTML page and the ``<head>`` of the response. If there are differences, Turbo Drive will reload the whole page.

En **app/views/layouts/application.html.erb**:

``<%= stylesheet_link_tag "application", "data-turbo-track": "reload" %>``

``<%= javascript_include_tag "application", "data-turbo-track": "reload", defer: true %>``

To **disable  Turbo Drive on a link or a form**, we need to add the ``data-turbo="false"`` data attribute on it.

To **disable Turbo Drive on the hole application**, en **app/javascript/application.js**

    import { Turbo } from "@hotwired/turbo-rails"
    Turbo.session.drive = false

**Turbo Frames** are independent pieces of a web page that can be appended, prepended, replaced, or removed without a complete page refresh and writing a single line of JavaScript!

With the combination of **Turbo Frames** and the new **Turbo Stream** format, we will be able to perform precise operations on pieces of our web pages without having to write a single line of JavaScript, therefore preserving the state of our web pages.


## 3.4 Sprockets

Sprockets: Rack-based asset packaging

**Sprockets** is a Ruby library for compiling and serving web assets. It features declarative dependency management for JavaScript and CSS assets, as well as a powerful preprocessor pipeline that allows you to write assets in languages like CoffeeScript, Sass and SCSS.

Sprockets parte de **config/manifest.js**

Si queremos que en aplication carge jquery desde node modules con ``//= require jquery``, en **config/initializer/asssets** tenemos que añadir la carperta **node_modules** al path de carga de assedets:

``Rails.application.config.assets.paths << Rails.root.join('node_modules')``

También:

``Rails.application.config.assets.paths << Rails.root.join('app/javascript')``

En **assets/config/manifest.js**

    //= link application.js 
    //= link_directory ../../javascript .js

Genera un archivo javascript por cada uno que se encuentre que termine en js.

**Nota**
Si una aplicación tiene

    gem "jsbundling-rails"
    # Bundle and transpile JavaScript [https://github.com/rails/    jsbundling-rails]

    gem "cssbundling-rails"
    # Bundle and process CSS [https://github.com/rails/   cssbundling-rails]

al ejecutar ``rails assets:precompile`` se enlaza con ``build`` y ``build:css`` de package.

Si no lo tiene, lo hará por Sprocket de forma tradicional

**Cuidado porque en desarrollo se puede mezclar todo, ya que ``rails s`` usar Sprocket para recompilar todo**

## 3.5 Tailwindcss template engine

Si tengo tailwind instalado como gema y quiero generar **templates normales**

``rails generate scaffold Gatos nombre:string apellidos:string --template-engine=erb``

También en **aplication.rb**: 

    config.generators.template_engine = :erb

Forzar engine tailwindcss:

``rails generate scaffold Elefantes nombre:string apellidos:string --template-engine=tailwindcss``

## 3.6 Import and exports javascript

**Must**: https://lenguajejs.com/javascript/modulos/import/

# 4. Tipos de aplicaciones rails

## 4.1 Opciones de instalación

    [--database=DATABASE] # Preconfigure for selected database (options: mysql/postgresql/sqlite3/oracle/sqlserver/jdbcmysql/jdbcsqlite3/  jdbcpostgresql/jdbc)

    [--skip-action-mailer], [--no-skip-action-mailer] # Skip Action Mailer files
    [--skip-action-mailbox], [--no-skip-action-mailbox] # Skip Action Mailbox gem
    [--skip-action-text], [--no-skip-action-text] # Skip Action Text gem
    [--skip-active-record], [--no-skip-active-record] # Skip Active Record files
    [--skip-active-job], [--no-skip-active-job] # Skip Active Job
    [--skip-active-storage], [--no-skip-active-storage] # Skip Active Storage files
    [--skip-action-cable], [--no-skip-action-cable] # Skip Action Cable files
    [--skip-asset-pipeline], [--no-skip-asset-pipeline] # Indicates when to generate skip asset pipeline
    [--asset-pipeline=ASSET_PIPELINE] # Choose your asset pipeline [options: sprockets (default), propshaft]
    [--skip-javascript], [--no-skip-javascript] # Skip JavaScript files
    [--skip-hotwire], [--no-skip-hotwire] # Skip Hotwire integration
    [--skip-jbuilder], [--no-skip-jbuilder] # Skip jbuilder gem
    [--skip-test], [--no-skip-test] # Skip test files
    [--skip-system-test], [--no-skip-system-test] # Skip system test files
    [--skip-bootsnap], [--no-skip-bootsnap] # Skip bootsnap gem

    [--api], [--no-api] # Preconfigure smaller stack for API only apps
    [--minimal], [--no-minimal] # Preconfigure a minimal rails app

  
    [--javascript=JAVASCRIPT] # Choose JavaScript [options: importmap (default), webpack, esbuild, rollup] 
    Use esbuild, rollup.js, or Webpack to **bundle your JavaScript**, then **deliver it via the asset pipeline** in Rails.
    **Añade gem "jsbundling-rails"**. 

    [--css=CSS] # Choose CSS processor [options: tailwind, bootstrap, bulma, postcss, sass] check https://github.com/rails/cssbundling-rails. 
    Añade **gem "cssbundling-rails"**

    [--skip-bundle], [--no-skip-bundle] # Don't run bundle install


## 4.2 Instalaciones mínimas

Por **defecto**:

``rails new myapp --minimal``

No se instalan: 
- action_mailer 
- action_mailbox 
- action_text 
- active_job 
- active_storage 
- action_cable 
- bootsnap 
- jbuilder 
- spring 
- system_tests 
- turbolinks 
- webpack


Una **mínimal a la carta**:
``rails new myapp
--skip-test --skip-system-test --skip-bootsnap --skip-jbuilder
--asset-pipeline=sprockets --javascript=esbuild --skip-hotwire
--skip-action-mailer --skip-action-mailbox --skip-action-text --skip-active-job --skip-active-storage --skip-action-cable``


# 5. Control de usuarios

**Fuente**: https://www.bcknd.tech/guia-de-autenticacion-y-autorizacion-en-ruby-on-rails/

## 5.1 Instalación de DEVISE
``gem 'devise'``
``bundle install``
``rails generate devise:install``

    ===============================================================================

    Depending on your application's configuration some manual setup may be required:

      1. Ensure you have defined default url options in your environments files. Here is an example of default_url_options appropriate for a development environment in config/environments/development.rb:

        config.action_mailer.default_url_options= { host: 'localhost', port: 3000 }

        In production, :host should be set to the actual host of your application.

         * Required for all applications. *

      2. Ensure you have defined root_url to *something* in your config/routes.rb.
         For example:

          root to: "home#index"

         * Not required for API-only Applications *

      3. Ensure you have flash messages in app/views/layouts/application.html.erb.
         For example:

          <p class="notice"><%= notice %></p>
          <p class="alert"><%= alert %></p>

         * Not required for API-only Applications *

      4. You can copy Devise views (for customization) to your app by running:

           rails g devise:views

         * Not required *

    ===============================================================================

``rails g devise:views``
``rails generate devise User``
``rails db:migrate``

##### Elaborar concerns ....
Ahora que ya está configurada la autenticación, protege las rutas y recursos:
before_action :authenticate_user!

AuthenticationConcern





PARA ELABORAR UN PANEL ADMIN A LA CARTA
https://dankim.io/rails-admin-dashboard-devise-bootstrap

We already have models for posts and categories. We can skip models when generating resources by using scaffold_controller generator that will create controllers and views only.

rails generate scaffold_controller admin/posts





#credentials

EDITOR='code --wait' rails credentials:edit