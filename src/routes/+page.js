/// The returned value of this function should act as a prop named 'data' for page.svelte
export const load = async (loadEvent) => {

    ///Do not use the fetch fucntion provided by windows [TBD]
	const { fetch } = loadEvent;
	const res = await connectFastApi(fetch);
	return res;
};


//Testing fast api connection[TBD]
const connectFastApi = async (fetch) => {
    ///Should be replaced by the real domain stored as env variable
	const res = await fetch('http://127.0.0.1:8000/main');
	const data = await res.json();
	return data;
};
