/* eslint-disable */
// @ts-nocheck
// This file was autogenerated by ethereum-abi-types-generator
import BN from 'bn.js';
import BigNumber from 'bignumber.js';
import {
  PromiEvent,
  TransactionReceipt,
  EventResponse,
  EventData,
  Web3ContractContext,
} from 'ethereum-abi-types-generator';

export interface CallOptions {
  from?: string;
  gasPrice?: string;
  gas?: number;
}

export interface SendOptions {
  from: string;
  value?: number | string | BN | BigNumber;
  gasPrice?: string;
  gas?: number;
}

export interface EstimateGasOptions {
  from?: string;
  value?: number | string | BN | BigNumber;
  gas?: number;
}

export interface MethodPayableReturnContext {
  send(options: SendOptions): PromiEvent<TransactionReceipt>;
  send(
    options: SendOptions,
    callback: (error: Error, result: any) => void,
  ): PromiEvent<TransactionReceipt>;
  estimateGas(options: EstimateGasOptions): Promise<number>;
  estimateGas(
    options: EstimateGasOptions,
    callback: (error: Error, result: any) => void,
  ): Promise<number>;
  encodeABI(): string;
}

export interface MethodConstantReturnContext<TCallReturn> {
  call(): Promise<TCallReturn>;
  call(options: CallOptions): Promise<TCallReturn>;
  call(
    options: CallOptions,
    callback: (error: Error, result: TCallReturn) => void,
  ): Promise<TCallReturn>;
  encodeABI(): string;
}

export interface MethodReturnContext extends MethodPayableReturnContext {}

export type ContractContext = Web3ContractContext<
  Vault,
  VaultMethodNames,
  VaultEventsContext,
  VaultEvents
>;
export type VaultEvents = 'EmergencyWithdrawn' | 'MerkleRootSet' | 'Withdrawn';
export interface VaultEventsContext {
  EmergencyWithdrawn(
    parameters: {
      filter?: {};
      fromBlock?: number;
      toBlock?: 'latest' | number;
      topics?: string[];
    },
    callback?: (error: Error, event: EventData) => void,
  ): EventResponse;
  MerkleRootSet(
    parameters: {
      filter?: {};
      fromBlock?: number;
      toBlock?: 'latest' | number;
      topics?: string[];
    },
    callback?: (error: Error, event: EventData) => void,
  ): EventResponse;
  Withdrawn(
    parameters: {
      filter?: {};
      fromBlock?: number;
      toBlock?: 'latest' | number;
      topics?: string[];
    },
    callback?: (error: Error, event: EventData) => void,
  ): EventResponse;
}
export type VaultMethodNames =
  | 'new'
  | 'auth'
  | 'batchWithdraw'
  | 'emergencyWithdraw'
  | 'lastClaimedEpoch'
  | 'merkleRoots'
  | 'setMerkleRoot'
  | 'verify';
export interface EmergencyWithdrawnEventEmittedResponse {
  user: string;
  amount: string;
}
export interface MerkleRootSetEventEmittedResponse {
  epoch: string;
  root: string | number[];
}
export interface WithdrawnEventEmittedResponse {
  user: string;
  amount: string;
  epoch: string;
}
export interface BatchWithdrawRequest {
  epoch: BigInt;
  amount: BigInt;
  proof: string | number[][];
}
export interface Vault {
  /**
   * Payable: false
   * Constant: false
   * StateMutability: nonpayable
   * Type: constructor
   * @param _auth Type: address, Indexed: false
   */
  'new'(_auth: string): MethodReturnContext;
  /**
   * Payable: false
   * Constant: true
   * StateMutability: view
   * Type: function
   */
  auth(): MethodConstantReturnContext<string>;
  /**
   * Payable: false
   * Constant: false
   * StateMutability: nonpayable
   * Type: function
   * @param payloads Type: tuple[], Indexed: false
   */
  batchWithdraw(payloads: BatchWithdrawRequest[]): MethodReturnContext;
  /**
   * Payable: false
   * Constant: false
   * StateMutability: nonpayable
   * Type: function
   * @param amount Type: uint256, Indexed: false
   */
  emergencyWithdraw(amount: string): MethodReturnContext;
  /**
   * Payable: false
   * Constant: true
   * StateMutability: view
   * Type: function
   * @param parameter0 Type: address, Indexed: false
   */
  lastClaimedEpoch(parameter0: string): MethodConstantReturnContext<string>;
  /**
   * Payable: false
   * Constant: true
   * StateMutability: view
   * Type: function
   * @param parameter0 Type: uint256, Indexed: false
   */
  merkleRoots(parameter0: string): MethodConstantReturnContext<string>;
  /**
   * Payable: false
   * Constant: false
   * StateMutability: nonpayable
   * Type: function
   * @param epoch Type: uint256, Indexed: false
   * @param root Type: bytes32, Indexed: false
   */
  setMerkleRoot(epoch: string, root: string | number[]): MethodReturnContext;
  /**
   * Payable: false
   * Constant: true
   * StateMutability: pure
   * Type: function
   * @param proof Type: bytes32[], Indexed: false
   * @param root Type: bytes32, Indexed: false
   * @param leaf Type: bytes32, Indexed: false
   */
  verify(
    proof: string | number[][],
    root: string | number[],
    leaf: string | number[],
  ): MethodConstantReturnContext<boolean>;
}
