<script>
	import Title from '../About/components/title.svelte';
	import Desc from './components/advantagesDescription.svelte';
	import Item from './components/items.svelte';
</script>

<section class="advantages lg:h-screen flex flex-col p-6">
	<Title pageTitle="Dunes aero’s advantages" elementHTML="h1" textColor="secondary" />
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
