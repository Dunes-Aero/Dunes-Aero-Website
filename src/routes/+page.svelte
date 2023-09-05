<script>
  import Hero from './Hero/+page.svelte'
  import About from './About/+page.svelte'
  import Contact from './Contact/+page.svelte'
</script>  
<Hero/>
<About/>
<Contact/>


  <style lang="postcss">
    :global(html) {
      background-color: theme(colors.gray.100);
    }
  </style>