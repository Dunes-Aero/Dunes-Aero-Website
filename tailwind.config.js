/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {

    extend: {
      colors: {
      
        'primary': 'var(--color-primary)',
        'primary-hover': 'var(--color-primary-hover)',
        'secondary': 'var(--color-secondary)',
        'secondary-hover': 'var(--color-secondary-hover)',
        'tertiary' :'var(--color-tertiary)',
        'tertiary-hover' :'var(--color-tertiary-hover)'},
      textColor:{
        skin:{
          primary: 'var(--color-primary)',
          secondary:  'var(--color-secondary)',
          tertiary:  'var(--color-tertiary)',
        }
      },
      fontFamily: {
  
        tenor: ['Tenor Sans'],
        joseph: ['Josefin Sans']
      }


    },
  },
  plugins: [],
}

