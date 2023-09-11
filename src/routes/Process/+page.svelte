<script>
	import Title from '../About/components/title.svelte';
	import Desc from './components/processDescription.svelte';
	import Line from './components/line.svelte';
</script>

<section
	class="our-process relative w-full pb-16 mx-auto bg-hero bg-no-repeat bg-cover bg-center items-center"
>
	<div class="lg:p-6 p-10">
		<Title pageTitle="Order Process" elementHTML="h1"  textColor="secondary" class="lg:w-full" />
	</div>

	<div>
		<Desc/>
	</div>

	<div class="lg:pt-6 2xl:pt-16 w-full"><Line /></div>
</section>

<style>
	@import '../About/global.css';

	.our-process {
		background-color: var(--color-primary);
	}
</style>
