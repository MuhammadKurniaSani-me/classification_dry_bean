function openDropDown() {
    const dropdowns = document.querySelectorAll(".dropdown");

    dropdowns.forEach(dropdown => {
        dropdown.addEventListener("click", ()=> {
            dropdown.querySelector(".arrow").classList.toggle("active");
            dropdown.querySelector(".dropdown-content").classList.toggle("active");
        });
    });
}

function DropDownFieldValues() {
    const fieldValues = document.querySelectorAll(".field .dropdown-content li");
    const classValues = document.querySelectorAll(".class .dropdown-content li");
    const classIdValues = document.querySelectorAll(".class-id .dropdown-content li");

    fieldValues.forEach(field => {
        field.addEventListener("click", ()=> {
            let choosenField= field.querySelector("p").textContent;
            document.querySelector(".field .label-dropdown").textContent = choosenField;
        })
    });
}

function DropDownClassValues() {
    const classValues = document.querySelectorAll(".class .dropdown-content li");

    classValues.forEach(classValue => {
        classValue.addEventListener("click", ()=> {
            let choosenClass = classValue.querySelector("p").textContent;
            document.querySelector(".class .label-dropdown").textContent = choosenClass;
        })
    });
}

function DropDownClassIdValues() {
    const classIdValues = document.querySelectorAll(".class-id .dropdown-content li");

    classIdValues.forEach(classIdValue => {
        classIdValue.addEventListener("click", ()=> {
            let choosenClassId= classIdValue.querySelector("p").textContent;
            document.querySelector(".class-id .label-dropdown").textContent = choosenClassId;
        })
    });
}

// run function
openDropDown();
DropDownFieldValues();
DropDownClassValues();
DropDownClassIdValues();
