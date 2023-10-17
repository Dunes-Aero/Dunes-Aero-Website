<script>
	import Title from '../About/components/title.svelte';
	import Desc from './components/advantagesDescription.svelte';
	import Item from './components/items.svelte';
</script>

<section class="advantages  flex flex-col h-[90vh] pb-2 p-6">
	<Title pageTitle="Why Dunes Aero?" elementHTML="h1" textColor="secondary" />
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
