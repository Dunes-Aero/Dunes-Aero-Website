<script>
	import Title from '../About/components/title.svelte';
	import Line from './components/line.svelte';
</script>

<section
	id="about"
	class="our-process relative w-full h-screen mx-auto bg-hero bg-no-repeat bg-cover bg-center items-center"
>
	<div class="p-16 w-full">
		<Title pageTitle="Our Process" elementHTML="h1" class="lg:w-full" />
	</div>

	<div class="pt-6"><Line /></div>
</section>

<style>
	@import '../About/global.css';

	.our-process {
		background-color: var(--color-secondary);
	}
</style>
