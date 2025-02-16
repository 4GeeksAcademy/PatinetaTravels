const getState = ({ getStore, getActions, setStore }) => {
    
    return {
        store: {
            message: null,
            demo: [
                {
                    title: "FIRST",
                    background: "white",
                    initial: "white"
                },
                {
                    title: "SECOND",
                    background: "white",
                    initial: "white"
                }
            ]
        },
        actions: {
            // Use getActions to call a function within a function
            exampleFunction: () => {
                getActions().changeColor(0, "green");
            },

            getMessage: async () => {
                try {
                    // fetching data from the backend
                    const resp = await fetch(`https://glorious-journey-7vrqjqg757q62wp5w-3001.app.github.dev//api/hello`);
                    const data = await resp.json();
                    setStore({ message: data.message });
                    // don't forget to return something, that is how the async resolves
                    return data;
                } catch (error) {
                    console.log("Error loading message from backend", error);
                }
            },

            changeColor: (index, color) => {
                // Get the store
                const store = getStore();

                // Loop the entire demo array to look for the respective index
                // and change its color
                const demo = store.demo.map((elm, i) => {
                    if (i === index) elm.background = color;
                    return elm;
                });

                // Reset the global store
                setStore({ demo: demo });
            },

            // SIGNUP.JS 

            signup: async (name, email, password) => {
                try {
                    const response = await fetch(`https://glorious-journey-7vrqjqg757q62wp5w-3001.app.github.dev//api/signup`, {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({ name, email, password })
                    });
            
                    const data = await response.json();
            
                    if (response.ok) {
                        alert("✅ Account created successfully!");
                        return true;
                    } else {
                        alert(`❌ Error: ${data.msg}`);
                        return false;
                    }
                } catch (error) {
                    console.error("Error during signup:", error);
                    alert("❌ Something went wrong, please try again.");
                    return false;
                }
            }
        }
    };
};

export default getState;
