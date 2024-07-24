/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './app/templates/**/*.html',
    './app/static/js/**/*.js',
  ],
  theme: {
    extend: {
      colors:{
        'dark':'#1e293b', 
        'primary':'#9EA0A5',
        'green': '#58C185'
      },
    },
  },
  plugins: [],
}

