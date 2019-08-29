import React, { Component } from 'react';
import FormUserDetails from './FormUserDetails';
import FormPersonalDetails from './FormPersonalDetails';
import Confirm from './Confirm';
import Success from './Success';


export class UserForm extends Component {
    state = {
        step:1,
        sysCode:"",
        tableName:"",
        attributeName:"",
        typeSize:"",
        description:"",
        example:""
    }

    // Next step
    nextStep = () => {
        const {step } = this.state;
        this.setState({step: step + 1});
    }

    // Previous step
    prevStep = () => {
        const {step } = this.state;
        this.setState({
            step: step - 1
        });
    }

    // Handle fields changes
    handleChange = input => e => {
        this.setState({[input]: e.target.value});
    }
    render() {
        const { step } = this.state;
        const { sysCode, tableName, attributeName, typeSize, description,
             example } = this.state;
        const values = { sysCode, tableName, attributeName, typeSize, description,
            example } 
        switch(step) {
            case 1: 
                return(
                    <FormUserDetails 
                       nextStep = {this.nextStep}
                        handleChange={this.handleChange}
                        values={values}
                    />
                )
            case 2:
                return(
                    <FormPersonalDetails 
                       nextStep = {this.nextStep}
                       prevStep = {this.prevStep}
                       handleChange={this.handleChange}
                       values={values}
                    />
                )
            case 3:
                return(
                    <Confirm 
                    nextStep = {this.nextStep}
                    prevStep = {this.prevStep}                    
                    values={values}
                 />
                )
            case 4:
                return(
                    <Success />
                )
        }
    } 
}
