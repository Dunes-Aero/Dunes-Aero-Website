<script>
	import Hero from './Hero/+page.svelte';
	import About from './About/+page.svelte';
	import Process from './Process/+page.svelte';
	import Contact from './Contact/+page.svelte';
	import Partners from './Partners/+page.svelte';
	import Solutions from './Solutions/+page.svelte';


	export let data=''
	$:msg = JSON.stringify(data)
</script>

<div class="main">

  <Hero />
	<Partners />
	<Solutions />
	<About />
	<Process />
	<Contact />

</div>

<style lang="postcss">
	:global(html) {
		background-color: theme(colors.gray.100);
	}

	.main {
		scroll-behavior: smooth;
	}
</style>
