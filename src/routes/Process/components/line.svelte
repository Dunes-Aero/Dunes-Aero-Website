<script>
	import Item from './item.svelte';
	import LineIcon from '$lib/assets/images/LineItem.svg';
</script>

<div class="container mx-auto relative">
	<!-- Image container -->
	<div class="grid justify-items-center">
		<img src={LineIcon} alt="" class="w-5" />
	</div>

	<!-- Absolute positioning for the "Item" components -->
	<div class="item-one absolute -top-8 lg:left-52">
		<Item textItem="Understand your business needs" />
	</div>
	<div class="item-two absolute top-40 transform -translate-y-1/2 right-80">
		<Item isRightLeft="yes" textItem="Finalize your order" />
	</div>
	<div class="item-three absolute bottom-8 left-60">
		<Item textItem="Order fulfilling and support" />
	</div>
</div>

<style>
	.container {
		height: 100%;
	}

	@media (max-width: 768px) {
		.container {
			display: flex;
			flex-direction: column;
			align-items: center; 
			justify-content: center; 
		}

		.item-one {
			text-align: center; 
		}

		.item-two {
			right: 23%; 
		}

		.item-three {
			left: 16%; 
		}
	}

	@media (min-width: 1300px) {
		.item-one {
			left: 25%;
		}
		.item-two {
			right: 30%;
		}
		.item-three {
			left: 26%;
		}
	}
</style>
