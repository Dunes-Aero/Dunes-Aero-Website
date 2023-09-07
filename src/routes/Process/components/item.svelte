<script>
	import ProcessIcon from '$lib/assets/images/GroupProcess.svg';
	export let isRightLeft;
    export let textItem;
</script>

<div class="container mx-auto flex items-center">
	<div class="item-back p-4 rounded-lg flex items-center">
		{#if isRightLeft == "yes"}
        <div class="mr-4">
            <p class="lg:text-lg text-item">{textItem}</p>
        </div>
			<img src={ProcessIcon} alt="" class="w-12 h-12" />

		{:else}

            <img src={ProcessIcon} alt="" class="w-12 h-12" />
			<div class="ml-4">
				<p class="text-lg text-item">{textItem}</p>
			</div>
		{/if}
	</div>
</div>

<style>
    .item-back {
        background-color: var(--color-primary);
        color: var(--color-secondary);
    }
	@media (max-width: 768px) {
		.text-item {
			font-size: small;
		}
	}
</style>