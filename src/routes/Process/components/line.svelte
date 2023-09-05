<script>
    import Item from './item.svelte'
    import LineIcon from '$lib/assets/images/LineItem.svg';

</script>

<div class="container mx-auto relative">
    <!-- Image container -->
    <div class="grid justify-items-center">
        <img src={LineIcon} alt="" class="w-5">
    </div>
    
    <!-- Absolute positioning for the "Item" components -->
    <div class="absolute -top-8 left-52">
        <Item textItem="Understand your business needs"/>
    </div>
    <div class="absolute top-40 transform -translate-y-1/2 right-80">
        <Item isRightLeft="yes" textItem="Finalize your order"/>
    </div>
    <div class="absolute bottom-8 left-60">
        <Item textItem="Order fulfilling and support"/>
    </div>
</div>


<style>
	/* ul {
		list-style: none;
		margin: 0;
		padding: 0;
		position: relative;
	}

	ul:before {
		content: '';
		display: inline-block;
		width: 2px;
		background: rgba(0, 0, 0, 0.22);
		position: absolute;
		top: 15px;
		right: 639px;
		height: calc(100% - 10px);
	}

	li {
		position: relative;
		padding-left: 15px;
		margin-bottom: 120px;
	}

	li:before {
		content: '';
		display: inline-block;
		width: 8px;
		height: 8px;
		background: red;
		position: absolute;
		left: 0;
		top: 5px;
		border-radius: 50%;
	} */
</style>
