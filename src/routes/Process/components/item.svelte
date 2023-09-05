<script>
	import ProcessIcon from '$lib/assets/images/GroupProcess.svg';
	export let isRightLeft;
    export let textItem;
</script>

<div class="container mx-auto flex items-center">
	<!-- Background div for the icon with text on the right -->
	<div class="item-back p-4 rounded-lg flex items-center">
		{#if isRightLeft == "yes"}
        <!-- Text on the right -->
        <div class="mr-4">
            <!-- Your text content here -->
            <p class="text-lg">{textItem}</p>
            <!-- Additional text or elements if needed -->
        </div>
			<!-- Icon (assuming you want to set a fixed width and height) -->
			<img src={ProcessIcon} alt="" class="w-12 h-12" />

		{:else}
			<!-- Text on the left -->
            <!-- Icon (assuming you want to set a fixed width and height) -->
            <img src={ProcessIcon} alt="" class="w-12 h-12" />
			<div class="ml-4">
				<!-- Your text content here -->
				<p class="text-lg">{textItem}</p>
				<!-- Additional text or elements if needed -->
			</div>
		{/if}
	</div>
</div>

<style>
    .item-back {
        background-color: var(--color-primary);
        color: var(--color-secondary);
    }
</style>