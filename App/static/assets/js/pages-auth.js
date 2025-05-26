/**
*  Pages Authentication
*/

'use strict';
const FormAuthenticationLoginAppicala = document.querySelector('#FormAuthenticationLoginAppicala');

document.addEventListener('DOMContentLoaded', function (e) {
    (function () {
        // Form validation for Add new record
        if (FormAuthenticationLoginAppicala) {
            const fv = FormValidation.formValidation(FormAuthenticationLoginAppicala, {
                fields: {
                    UserNameLoginAppicala: {
                        validators: {
                            notEmpty: {
                                message: 'Por favor ingresar el usuario'
                            },
                            stringLength: {
                                min: 1,
                                message: 'Usuario debe tener más de 1 caracteres'
                            }
                        }
                    },
                    UserEmailLoginAppicala: {
                        validators: {
                            notEmpty: {
                                message: 'Por favor ingresar su correo'
                            },
                            emailAddress: {
                                message: 'Por favor ingresar un correo valido'
                            }
                        }
                    },
                    'UserNameConfirmLoginAppicala': {
                        validators: {
                            notEmpty: {
                                message: 'Por favor confirmar el usuario'
                            },
                            stringLength: {
                                min: 1,
                                message: 'Usuario debe tener más de 1 caracteres'
                            }
                        }
                    },
                    PasswordLoginAppicala: {
                        validators: {
                            notEmpty: {
                                message: 'Por favor ingresar su contraseña'
                            },
                            stringLength: {
                                min: 3,
                                message: 'Contraseña debe tener más de 3 caracteres'
                            }
                        }
                    },
                    'PasswordConfirmLoginAppicala': {
                        validators: {
                            notEmpty: {
                                message: 'Por favor confirmar su contraseña'
                            },
                            identical: {
                                compare: function () {
                                    return FormAuthenticationLoginAppicala.querySelector('[name="PasswordLoginAppicala"]').value;
                                },
                                message: 'La contraseña y su confirmación no son lo mismo.'
                            },
                            stringLength: {
                                min: 3,
                                message: 'Contraseña debe tener más de 3 caracteres'
                            }
                        }
                    },
                    terms: {
                        validators: {
                            notEmpty: {
                                message: 'Por favor acepta términos y condiciones'
                            }
                        }
                    }
                },
                plugins: {
                    trigger: new FormValidation.plugins.Trigger(),
                    bootstrap5: new FormValidation.plugins.Bootstrap5({
                        eleValidClass: '',
                        rowSelector: '.mb-6'
                    }),
                    /* submitButton: new FormValidation.plugins.SubmitButton(),
                    defaultSubmit: new FormValidation.plugins.DefaultSubmit(), */
                    autoFocus: new FormValidation.plugins.AutoFocus()
                },
                init: instance => {
                    instance.on('plugins.message.placed', function (e) {
                        if (e.element.parentElement.classList.contains('input-group')) {
                            e.element.parentElement.insertAdjacentElement('afterend', e.messageElement);
                        }
                    });
                }
            });
        }

        //  Two Steps Verification
        const numeralMask = document.querySelectorAll('.numeral-mask');

        // Verification masking
        if (numeralMask.length) {
            numeralMask.forEach(e => {
                new Cleave(e, {
                    numeral: true
                });
            });
        }
    })();
});
