<script>
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
</script>

<div class="container mx-auto flex items-center">
	<div class="item-box item-back lg:p-4 p-2 rounded-lg flex items-center">
		{#if isRightLeft == 'yes'}
			<div class="mr-4">
				{#each textItems as textItem}
					<p class="lg:text-lg text-item">{textItem}</p>
				{/each}
			</div>
			<img src={selectedIcon} alt="" class="img-item w-16 h-16" />
		{:else}
			<img src={selectedIcon} alt="" class="img-item w-16 h-16" />
			<div class="ml-4">
				{#each textItems as textItem}
					<p class="lg:text-lg text-item">{textItem}</p>
				{/each}
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
	@media (max-width: 768px) {
		.text-item {
			font-size: 10px;
		}
		.img-item {
			width: 35px;
			height: 35px;
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
	}
</style>
