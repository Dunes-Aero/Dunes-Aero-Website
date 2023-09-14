<script>
	import Item from './item.svelte';
	import LineIcon from '$lib/assets/images/Timeline.svg';
</script>

<div class="">
	<!-- Image container -->
	<!-- <div class="flex justify-center">
		<img src={LineIcon} alt="" class="w-5 line-small" />
	</div> -->
	<div class="">
		<img src={LineIcon} alt="" class="w-5 line-small" />
	</div>

	<!-- Absolute positioning for the "Item" components -->
	<!-- <div class="item-one absolute">
		<Item isRightLeft="yes" textItems={['Contact Us']} iconName="contact" />
	</div>
	<div class="item-two absolute">
		<Item textItems={['Understanding your', ' business needs']} iconName="business" />
	</div>
	<div class="item-three absolute">
		<Item isRightLeft="yes" textItems={['Finalize your order']} iconName="order" />
	</div>
	<div class="item-four absolute">
		<Item textItems={['Order fulfilling and', 'support']} iconName="support" />
	</div> -->
</div>

<style>
	/* .item-one {
		top: -38px;
		right: 280px;
	}
	.item-two {
		top: 77px;
		left: 270px;
	}
	.item-three {
		top: 222px;
		right: 250px;
	}
	.item-four {
		top: 346px;
		left: 270px;
	} */

	@media (max-width: 768px) {
		.line-small {
			/* width: 18px; */
		}
		/* .item-one { 
			top: -20px;
			right: 250px;
		}
		.item-two {
			top: 65px;
			left: 230px;
		}
		.item-three {
			top: 175px;
			right: 235px;
		}
		.item-four {
			top: 265px;
			left: 230px;
		} */
	}

	@media (min-width: 1300px) {
		.line-small {
			width: 25px;
		}
		/* .item-one {
			top: -40px;
			right: 500px;
		}
		.item-two {
			top: 100px;
			left: 490px;
		}
		.item-three {
			top: 280px;
			right:470px;
		}
		.item-four {
			top: 440px;
			left: 490px;
		} */
	}
</style>
