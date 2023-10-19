<script>
	import Carousel from 'svelte-carousel';

	import { browser } from '$app/environment';
</script>

<div class=" bg-primary">
	{#if browser}
		<div class=" bg-primary mt-10">
			<Carousel particlesToShow={5} particlesToScroll={2}>
				<div class="flex flex-col items-center">
					<img src="src/lib/assets/images/adv1.svg" class="product-thumb px-10" alt="1" />
					<p class="text-secondary break-words text-center my-3">
						Faster Communication & <br /> Collaborations
					</p>
				</div>

				<div class="flex flex-col items-center">
					<img src="src/lib/assets/images/adv2.svg" class="product-thumb px-10" alt="2" />
					<p class="text-secondary break-words text-center my-3">Local Support and Expertise</p>
				</div>

				<div class="flex flex-col items-center">
					<img src="src/lib/assets/images/adv3.svg" class="product-thumb px-10" alt="3" />

					<p class="text-secondary break-words text-center my-3">Enhanced Reliability</p>
				</div>

				<div class="flex flex-col items-center">
					<img src="src/lib/assets/images/adv4.svg" class="product-thumb px-10" alt="4" />
					<p class="text-secondary break-words text-center my-3">
						Extensive support & <br /> maintenance
					</p>
				</div>

				<div class="flex flex-col items-center">
					<img src="src/lib/assets/images/adv5.svg" class="product-thumb px-10" alt="5" />
					<p class="text-secondary break-words text-center my-3">Tailored Solutions</p>
				</div>

				<div class="flex flex-col items-center">
					<img src="src/lib/assets/images/adv6.svg" class="product-thumb px-10" alt="6" />
					<p class="text-secondary break-words text-center my-3">Advanced AI detection software</p>
				</div>

				<div class="flex flex-col items-center">
					<img src="src/lib/assets/images/adv7.svg" class="product-thumb px-10" alt="7" />
					<p class="text-secondary break-words text-center my-3">Regulatory compliance</p>
				</div>

				<div class="flex flex-col items-center">
					<img src="src/lib/assets/images/adv8.svg" class="product-thumb px-10" alt="8" />
					<p class="text-secondary break-words text-center my-3">Training programs</p>
				</div>
			</Carousel>
		</div>
	{/if}
</div>

<style>
	@import '../../About/global.css';
</style>
