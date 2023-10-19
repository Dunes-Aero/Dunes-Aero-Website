<script>
	import { quintOut } from 'svelte/easing';
	import { fade, draw, fly } from 'svelte/transition';
	import { expand } from '$lib/utils/custom-transitions.js';

	import { inview } from 'svelte-inview';
	let visible;
	const options = {};
	const handleChange = ({ detail }) => {
		visible = detail.inView;

	};
</script>

<div use:inview={options} on:inview_change={handleChange}>
	{#if visible}
		<svg
			width="30"
			height="520"
			viewBox="0 0 30 520"
			fill="none"
			xmlns="http://www.w3.org/2000/svg"
		>
			<line
            transition:draw="{{delay:150, duration: 1000, easing: quintOut}}"
				style="stroke: #EBE3D2; fill: #EBE3D2; stroke-width: 4;"
				x1="14"
				y1="3"
				x2="14"
				y2="510"
			/>
			<circle
				in:fade|global={{ delay: 800 + 950, duration: 800 }}
				cx="14.5125"
				cy="498"
				r="14.5125"
				fill="black"
			/>
			<circle
				in:fade|global={{ delay: 800 + 650, duration: 800 }}
				cx="14.5125"
				cy="320"
				r="14.5125"
				fill="#636363"
			/>
			<circle
				in:fade|global={{ delay: 800 + 350, duration: 800 }}
				cx="14.5125"
				cy="148.512"
				r="14.5125"
				fill="#A5A5A5"
			/>
			<circle
				in:fade|global={{ delay: 800 + 150, duration: 800 }}
				cx="14.5125"
				cy="14.5125"
				r="14.5125"
				fill="#EFEFEF"
			/>
		</svg>
	{/if}
</div>
