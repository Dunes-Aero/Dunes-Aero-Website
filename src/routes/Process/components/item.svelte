<script>
	import GModel from './boxModel.svelte';
	import contactIcon from '$lib/assets/images/contactUs.svg';
	import businessIcon from '$lib/assets/images/business.svg';
	import orderIcon from '$lib/assets/images/order.svg';
	import supportIcon from '$lib/assets/images/support.svg';
	export let isRightLeft;
	export let textItems;
	export let iconName;
	// Create a variable to store the selected icon
	let selectedIcon;

	switch (iconName) {
		case 'contact':
			selectedIcon = contactIcon;
			break;
		case 'business':
			selectedIcon = businessIcon;
			break;
		case 'order':
			selectedIcon = orderIcon;
			break;
		case 'support':
			selectedIcon = supportIcon;
			break;
	}

	let showModel = false;
	const handleClose = () => {
		showModel = false;
	};

	export let titleContent;
	export let textContent;
</script>

<GModel show={showModel} titleContent={titleContent} textContent={textContent} on:close={handleClose} />

<div class="container mx-auto flex items-center">
	<div class="item-box item-back md:p-4 p-2 rounded-lg flex items-center">
		{#if isRightLeft == 'yes'}
			<div class="mr-4">
				{#each textItems as textItem}
					<p class="lg:text-lg text-item">{textItem}</p>
				{/each}
				<div class="read-more">
					<button
						class="text-more underline underline-offset-1 cursor-pointer pt-2"
						on:click={() => (showModel = true)}>Read more</button
					>
				</div>
			</div>
			<img src={selectedIcon} alt="" class="img-item md:w-16" />
		{:else}
			<img src={selectedIcon} alt="" class="img-item md:w-16" />
			<div class="ml-4">
				{#each textItems as textItem}
					<p class="lg:text-lg text-item">{textItem}</p>
				{/each}
				<div class="read-more">
					<button
						class="text-more underline underline-offset-1 cursor-pointer pt-2"
						on:click={() => (showModel = true)}>Read more</button
					>
				</div>
			</div>
		{/if}
	</div>
</div>

<style>
	.item-back {
		color: var(--color-secondary);
	}
	.item-box {
		/* width: 350px; */
		text-align: center;
	}
	.text-more {
		font-size: 8px;
	}
	@media (max-width: 768px) {
		.text-item {
			font-size: 10px;
		}
		.img-item {
			width: 30px;
			height: 30px;
		}
		.text-more {
			font-size: 6px;
		}
	}

	@media (min-width: 1300px) {
		.text-item {
			font-size: 22px;
		}
		.img-item {
			width: 75px;
			height: 75px;
		}
		.text-more {
			font-size: 12px;
		}
	}
</style>
