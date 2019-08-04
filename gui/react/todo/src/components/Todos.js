import React, {Component} from 'react';
import TodoItem from './TodoItems';
import PropTypes from 'prop-types';

class Todos extends Component {
   render() {
        return this.props.todos.map((todo) =>(
           <TodoItem key={todo.id} todo={todo} /> 
        ));
   }
}

// Property types
// Todos.PropTypes = {}
//    todos: PropTypes.array.isRequired
//}
export default Todos;
