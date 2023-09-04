/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      textColor:{
        skin:{
          primary: 'var(--color-primary)',
          secondary:  'var(--color-secondary)',
        }
      }


    },
  },
  plugins: [],
}

