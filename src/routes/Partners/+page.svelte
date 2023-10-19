<script>
	import Subtitle from '../../lib/components/Subtitle.svelte';
	import Carousel from 'svelte-carousel';
	import ResizeObserver from 'resize-observer-polyfill';
	import { onMount } from 'svelte';
	import { browser } from '$app/environment';
</script>

{#if browser}
	<section id="partners" class="partners ">
		<div class="slider">
			<Subtitle>SUPPORTED BY</Subtitle>

			<Carousel
				autoplayDuration={10}
				duration={10000}
				autoplay
				timingFunction="linear"
				dots={false}
				arrows={false}
				swiping={false}
				infinite={true}
			>
				<div class="flex w-full space-x-4 sm:space-x-0 justify-around px-4 sm:px-0 items-center">
					<div class="flex-initial">
						<img src="/src/lib/assets/images/MCIT.svg" alt="MCIT" />
					</div>
					<div class="flex-initial">
						<img src="/src/lib/assets/images/GACA.svg" alt="GACA" />
					</div>
					<div class="flex-initial">
						<img src="/src/lib/assets/images/KACST.svg" alt="KACST" />
					</div>
				</div>
				<div class="flex w-full space-x-4 sm:space-x-0 justify-around px-4 sm:px-0 items-center">
					<div class="flex-initial">
						<img src="/src/lib/assets/images/NTDP.svg" alt="NTDP" />
					</div>
					<div class="flex-initial">
						<img src="/src/lib/assets/images/GACA.svg" alt="GACA" />
					</div>
					<div class="flex-initial">
						<img src="/src/lib/assets/images/SFCPD.svg" alt="SFCPD" />
					</div>
				</div>
			</Carousel>
		</div>
	</section>
{/if}

<style>
	.slider {
		height: 235px;
		margin: auto;
		overflow: hidden;
		position: relative;
		background-color: var(--color-secondary);
	}
</style>
