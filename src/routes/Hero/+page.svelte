<script>
	import Navbar from './Navbar.svelte';
	import Intro from './Intro.svelte';
</script>

<section
	id="hero"
	class="relative w-full h-screen mx-auto bg-hero bg-no-repeat bg-cover bg-center items-center flex"
>
	<Navbar />
	<Intro />
</section>

<style>
	.bg-hero {
		background-image: url('./src/lib/assets/images/hero-bg.png');
		background-color: black;
	}
</style>
