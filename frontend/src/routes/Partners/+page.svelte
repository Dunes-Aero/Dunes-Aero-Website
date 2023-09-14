<script>
	import Subtitle from '../../lib/components/Subtitle.svelte';
	import Carousel from 'svelte-carousel';
	import ResizeObserver from 'resize-observer-polyfill';
	import { onMount } from 'svelte';
	import { browser } from '$app/environment';

	let boxEl;
	let boxWidth;
	// Add the observer when component mounts and cleanup after
	onMount(() => {
		const resizeObserver = new ResizeObserver((entries) => {
			// We're only watching one element
			const entry = entries.at(0);

			//Get the block size
			boxEl = entry.contentBoxSize[0].blockSize;
		});

		resizeObserver.observe(boxEl);

		// This callback cleans up the observer
		return () => resizeObserver.unobserve(boxEl);
	});
</script>

{#if browser}
	<section id="partners" class="partners">
		<div class="slider">
			<Subtitle>SUPPORTED BY</Subtitle>

			<Carousel
				autoplayDuration={10}
				duration={5000}
				autoplay
				timingFunction="linear"
				dots={false}
				arrows={false}
				swiping={false}
				infinite={true}
				bind:this={boxEl}
			 
			>
				<div class=" flex sm:overflow-hidden  ">
					<img src="src\lib\assets\images\GACA.svg" alt="logo" height="100" class="mx-8" width="250" />

					<img src="src\lib\assets\images\KACST.svg" alt="logo" height="100" class="mx-8" width="250" />

					<img src="src\lib\assets\images\MCIT.svg" alt="logo" height="100" class="mx-8" width="250" />

					<img src="src\lib\assets\images\NTDP.svg" alt="logo" height="100" class="mx-8" width="250" />

					<img src="src\lib\assets\images\SFCPD.svg" alt="logo" height="100" class="mx-8" width="250" />

				</div>
			</Carousel>
		</div>
	</section>
{/if}

<style>
	.title {
		margin-top: 40px;
		text-align: center;
		font-size: 28px;
		font-weight: 600;
	}

	.slider {
		height: 235px;
		margin: auto;
		overflow: hidden;
		position: relative;

		background-color: var(--color-secondary);
	}
 
 
</style>
