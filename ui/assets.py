from django_assets import Bundle, register


css_main = Bundle(
    'bootstrap/dist/css/bootstrap.css',
    'djangular/css/styles.css',
    'font-awesome/css/font-awesome.css',

    filters=('cssrewrite', 'yui_css',),
    output='compiled-assets/gen/css_main.$(version)s.css'
)

register('css_main', css_main)

js_main = Bundle(
    'jquery/dist/jquery.min.js',
    'lodash/lodash.min.js',
    'angular/angular.min.js',
    'angular-bootstrap/ui-bootstrap-tpls.min.js',
    'angular-route/angular-route.min.js',
    'angular-resource/angular-resource.min.js',
    'angular-cookies/angular-cookies.min.js',
    'angular-animate/angular-animate.min.js',

    'djangular/js/django-angular.js',

    'js/angular-app/module.js',
    'js/angular-app/resources.js',
    'js/angular-app/controllers.js',

    filters='closure_js',
    output='compiled-assets/gen/js_main.%(version)s.js')

register('js_main', js_main)
