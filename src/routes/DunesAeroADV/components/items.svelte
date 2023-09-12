<script>
	import firstDist from '$lib/assets/images/Our Distinguishment 3.png';
	import secondDist from '$lib/assets/images/Our Distinguishment 1.png';
	import thirdDist from '$lib/assets/images/Our Distinguishment 4.png';
	import fourthDist from '$lib/assets/images/Our Distinguishment 2.png';
</script>

<div
	class="flex sm:flex-wrap items-center justify-center p-6 md:flex-row space-x-16 md:space-x-4 2xl:space-x-10"
>
	<div
		class="md:flex
    "
	>
		<img src={firstDist} alt="" class="w-32 md:w-40 2xl:w-80 h-auto pt-6 2xl:p-10" />
		<img src={secondDist} alt="" class="w-32 md:w-40 2xl:w-80 h-auto pt-6 2xl:p-10" />
	</div>
	<div class="md:flex">
		<img src={thirdDist} alt="" class="w-24 md:w-28 2xl:w-56 h-auto p-2 2xl:p-10" />
		<img src={fourthDist} alt="" class="w-28 md:w-36 2xl:w-64 h-auto pt-6 2xl:p-10" />
	</div>
</div>

<style>
	@import '../../About/global.css';
</style>
