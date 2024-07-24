/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './app/templates/**/*.html',
    './app/static/js/**/*.js',
  ],
  theme: {
    extend: {
      colors:{
        'dark':'#20262E', 
        'primary':'#CBCBCB',
        'green': '#58C185'
      },
    },
  },
  plugins: [],
}

