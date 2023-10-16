<script>
	import Title from './components/title.svelte';
	import Desc from './components/aboutDescription.svelte';
	import { fade } from 'svelte/transition'
</script>

<section
	id="about"
	class="main-page about sm:h-screen bg-cover bg-center bg-no-repeat flex flex-col justify-center"
>
	<div class="mb-4 text-center">
		<Title pageTitle="About Us" elementHTML="h1" textColor="secondary" />
	</div>
	<div class="text-center" transition:fade>
		<Desc />
	</div>
</section>

<style>
	@import './global.css';

	.about {
		background-image: url('$lib/assets/images/Bacground.png');
		/* padding: 75px;
        width: 100%; */
	}

	@media (max-width: 768px) {
		.about {
			padding: 50px;
		}
	}
</style>
