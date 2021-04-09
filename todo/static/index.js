function removeTodo(todoId) {
    fetch("/remove_todo", {
        method: "POST",
        body: JSON.stringify({ todoId: todoId }),
    }).then((_res) => {
        window.location.href = "/";
    });
}
console.log("Poda potta");