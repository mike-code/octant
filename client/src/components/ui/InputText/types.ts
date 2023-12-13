import { ChangeEvent, FocusEventHandler, HTMLAttributes, ReactNode } from 'react';

export const INPUT_TEXT_VARIANTS = ['borderless', 'boxRounded', 'simple'] as const;
export type InputTextVariant = (typeof INPUT_TEXT_VARIANTS)[number];

export default interface InputTextProps {
  autocomplete?: string;
  className?: string;
  dataTest?: string;
  error?: string;
  inputMode?: HTMLAttributes<HTMLInputElement>['inputMode'];
  isButtonClearVisible?: boolean;
  isDisabled?: boolean;
  isErrorInlineVisible?: boolean;
  label?: string | ReactNode;
  name?: string;
  onBlur?: FocusEventHandler<HTMLInputElement>;
  onChange?: (event: ChangeEvent<HTMLInputElement>) => void;
  onClear?: () => void;
  onFocus?: FocusEventHandler<HTMLInputElement>;
  placeholder?: string;
  shouldAutoFocusAndSelect?: boolean;
  showLoader?: boolean;
  suffix?: string;
  suffixClassName?: string;
  textAlign?: 'left' | 'center';
  value?: string;
  variant?: InputTextVariant;
}