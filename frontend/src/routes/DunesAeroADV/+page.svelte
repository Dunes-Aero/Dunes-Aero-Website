<script>
	import Title from '../About/components/title.svelte';
	import Desc from './components/advantagesDescription.svelte';
	import Item from './components/items.svelte';
</script>

<section class="advantages  flex flex-col h-screen pb-2 p-6">
	<h1 class="xl:text-5xl lg:text-4xl text-2xl text-center text-secondary   font-joseph	 my-10">Why Dunes Aero?</h1>
	<div class="flex flex-col justify-center items-center 2xl:pt-10 pb-10 ">
		<Desc />
	</div>
    <div class="items 2xlg:pt-14">
        <Item />
    </div>
</section>

<style>
	@import '../About/global.css';

	.advantages {
		background-color: var(--color-primary);
	}
</style>
