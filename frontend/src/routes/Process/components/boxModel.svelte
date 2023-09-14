<script>
	import { fade } from 'svelte/transition';
	import { slide } from 'svelte/transition';
	import { quintOut } from 'svelte/easing';
	import { createEventDispatcher } from 'svelte';
	const dispatch = createEventDispatcher();
	export let show = true;
	const close = () => {
		show = false;
		dispatch('close');
	};
    export let titleContent;
    export let textContent;
</script>

{#if show}
	<!-- svelte-ignore a11y-click-events-have-key-events -->
	<div class="fixed top-0 left-0 w-full h-full bg-black bg-opacity-75 z-50" on:click={close}>
		<div class="box-item mx-auto my-52 md:my-32 2xl:my-52 max-w-sm rounded-lg shadow-xl p-10" on:click|stopPropagation>
			<h3 class="text-lg mb-4">{titleContent}</h3>
			<p class="text-box mb-4">
				{textContent}
			</p>
			<div class="flex justify-end">
				<button
					transition:slide={{ delay: 25, duration: 150, easing: quintOut, axis: 'y' }}
					class="btn-box text-white px-4 py-2 rounded-lg"
					on:click={close}
				>
					Close
				</button>
			</div>
		</div>
	</div>
{/if}

<style>
	.box-item {
		background-color: var(--color-secondary);
	}
	.text-box {
		color: var(--color-primary);
	}
	.btn-box {
		background-color: var(--color-primary);
	}
	.btn-box:hover {
		opacity: 75%;
	}
</style>
