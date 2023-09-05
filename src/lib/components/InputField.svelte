<script>
    export let name=''
    export let placeholder=''
    export let type='text'
    export let mode =true  //True as in light mode, false for dark
    let color = mode?'secondary':'primary'
</script>


<div class="mb-4">
    <label
        class={`block mb-2 text-md font-joseph font-meduium text-${color}`}
        for={name}
    >
       <slot/>
    </label>
    <input
        class={`bg-transparent px-3 py-2 mb-3 text-md leading-tight font-joseph font-medium text-${color} border-b border-${color} rounded shadow appearance-none focus:outline-none focus:shadow-outline`}
        id={name}
        type={type}
        placeholder={placeholder}
    />
</div>

