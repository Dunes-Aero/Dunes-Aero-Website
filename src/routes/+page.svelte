<script>
  import Hero from './Hero/+page.svelte'
  import About from './About/+page.svelte'
</script>  
<Hero/>
<About/>
  <style lang="postcss">
    :global(html) {
      background-color: theme(colors.gray.100);
    }
  </style>